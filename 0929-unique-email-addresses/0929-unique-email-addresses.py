class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        email_set = set()
        
        for email in emails:
            email_split = email.split("@")
            local = email_split[0]
            domain = email_split[1]
            target = local.split("+")[0]
            alias = "".join(target.split("."))
            email_set.add((alias, domain))
        
        return len(email_set)
            