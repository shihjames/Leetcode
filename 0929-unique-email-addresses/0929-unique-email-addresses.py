"""
Time = O(nm)
Space = O(nm)
"""
class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        email_set = set()
        
        for email in emails:
            local, domain = email.split("@")
            target = local.split("+")[0]
            alias = "".join(target.split("."))
            email_set.add((alias+"@"+domain))
        
        return len(email_set)
            