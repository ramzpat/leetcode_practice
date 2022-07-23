# https://leetcode.com/problems/subdomain-visit-count/

from collections import defaultdict
from typing import Dict, List

class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        domain_t = str
        cntRep:Dict[domain_t, int] = {}
        
        for rep_domain in cpdomains:
          [rep, domain] = rep_domain.split(" ")
          sub_domains = domain.split(".")
          for i in range(len(sub_domains)):
            target_domain = ".".join(sub_domains[i:])
            cntRep[target_domain] = cntRep.get(target_domain, 0) +  int(rep)
        
        return [str(cntRep[domain]) + " " + domain for domain in cntRep.keys()]