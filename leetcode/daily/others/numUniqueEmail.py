from typing import List

class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        for idx, email in enumerate(emails):
            local, domain = email.split("@")
            local = local.split("+")[0].replace(".", "")
            
            emails[idx] = f"{local}@{domain}"
            
        return len(set(emails))

Solution().numUniqueEmails(emails=["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"])
Solution().numUniqueEmails(emails=["test.email+alex@leetcode.com", "test.email@leetcode.com"])
