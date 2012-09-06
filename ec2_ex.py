import boto
ec2 = boto.connect_ec2()

for r in ec2.get_all_instances():
    if r.id == reservation.id:
        break
print r.instances[0].public_dns_name  # output: ec2-184-73-24-97.compute-1.amazonaws.com

