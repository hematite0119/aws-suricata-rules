# awscli version 1
# aws network-firewall list-rule-groups --output text | cut -f 3 > test.txt

import json

f = open('/home/ec2-user/environment/aws-network-firewall-rulegroups-with-proofpoints-emerging-threats-open-ruleset/test.txt', 'r', encoding="utf-8")
rules_list = []
for rule in f:
    rule = rule.replace("\n", "")
    rules_list.append(rule)
f.close()

#print(str(rules_list).replace("\'",""))


#j_rules_list=json.dumps(rules_list)
f = open('/home/ec2-user/environment/aws-network-firewall-rulegroups-with-proofpoints-emerging-threats-open-ruleset/rules_list.txt', 'w', encoding="utf-8")
f.write(str(rules_list).replace("\'", ""))
f.close()
