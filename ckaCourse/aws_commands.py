
# Instance "primary node" : i-0bc9ada7a3038e2fd
# ssh -i ~/.ssh/cka_course_key.pem ubuntu@15.237.187.87
# ssh -i ~/.ssh/cka_course_key.pem ubuntu@ec2-13-39-155-103.eu-west-3.compute.amazonaws.com


# Instance "secondary node" (worker) : i-0fbad5257250dd8ba
# ssh -i ~/.ssh/cka_course_key.pem ubuntu@13.38.55.125
# ssh -i ~/.ssh/cka_course_key.pem ubuntu@ec2-35-180-139-30.eu-west-3.compute.amazonaws.com


kubectl create token
kubectl get node
kubectl describe node ip-172-31-36-187

kubectl create deployment nginx --image=nginx
kubectl get deployment nginx -o yaml > first.yaml
kubectl delete deployment nginx
kubectl create -f first.yaml


