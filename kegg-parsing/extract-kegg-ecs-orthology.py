#!/usr/bin/env python

import sys, re, datetime

f = open(sys.argv[1])   # kegg reaction file
o = open(sys.argv[2], "w") 

o.write("#Generated by \"%s\" on %s\n" % (" ".join(sys.argv), datetime.datetime.now()))

reec = re.compile("([\d\-]+\.[\d\-]+\.[\d\-]+\.[\d\-]+)")

id = None
ec = set()
block = None
ec2r = {}
for s in f:
    if s[0] != " ":
        block = None
        if s.startswith("ENTRY"):
            id = s.strip().split()[1]
        elif s.startswith("ENZYME"):
            ec = set(s.strip()[12:].split())
            block = "enzyme"
        elif s.startswith("ORTHOLOGY"):
            ec.update(reec.findall(s))
            block = "orthology"
        elif s.startswith("///"):
            assert(id)
            if len(ec) == 0:
                ec = set(["?"])
            #o.write("%s\t%s\n" % (id, ",".join(ec)))
            for e in ec:
                if e not in ec2r:
                    ec2r[e] = set()
                ec2r[e].add(id)
            id = None
            ec = set()
    else:
        if block == "enzyme":
            ec.update(s[12:].split())
        elif block == "orthology":
            ec.update(reec.findall(s))

k = ec2r.keys()
k.sort()
for e in k:
    rs = list(ec2r[e])
    rs.sort()
    o.write("%s\t%s\n" % (e, ",".join(rs)))