# H1 Cloud-Init Files

These are the cloud-init files for creating the Rancher Management Node and the Rancher Node.

- user-data - Rancher Management node
- user-data2 - Rancher K8s Node


rancher-mgmt 192.168.1.215
rancher-node 192.168.1.214

rancher-mgmt (web console) -> admin p: WoQsWBYQF8rsg@TJLR 

Registration Command for nodes:
sudo docker run -d --privileged --restart=unless-stopped --net=host -v /etc/kubernetes:/etc/kubernetes -v /var/run:/var/run  rancher/rancher-agent:v2.5.7 --server https://192.168.1.215 --token fknm5t7vpc7dkxgvmc7rkr5lr2rmk77qqg7ph2w524tnvtncq7xrsl --ca-checksum 6e1b960c369230e13bbb9d08142cfeda839c795ef306bd7a7217ad0e4704e256 --etcd --controlplane --worker

TODO: setup node on office laptop

Commands:
ku get all -A #show everything running
ku describe ds -n metallb-system #check the deamonSet
k9s

Inginx IP 192.168.1.240