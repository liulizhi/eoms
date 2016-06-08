#-*- coding:utf-8 -*-
'''
Created on 2016-6-8

@author: QiRui.Su schangech@gmail.com
'''
import sys
import json
import urllib2
from urllib2 import URLError
from zabbix_auth import Zabbix_Auth

class Zabbix_Utils:

    def __init__(self):
        self.url = 'http://zabbix.light.fang.com/api_jsonrpc.php'
        self.header = {"Content-Type":"application/json"}

    def host_get(self,hostip=''): 
        data=json.dumps({
                "jsonrpc": "2.0",
                "method": "host.get",
                "params": {
                          "output": "extend",
                          "filter":{"ip":hostip} 
                          },
                "auth": Zabbix_Auth().user_login(),
                "id": 1
                })
        request = urllib2.Request(self.url,data) 
        for key in self.header: 
            request.add_header(key, self.header[key]) 
        try: 
            result = urllib2.urlopen(request) 
        except URLError as e: 
            if hasattr(e, 'reason'): 
                print 'Reason: ', e.reason 
            elif hasattr(e, 'code'): 
                print 'Error code: ', e.code 
        else: 
            response = json.loads(result.read()) 
            result.close()
            hostlist = []
            for host in response['result']:      
                hostlist.append(host['name'])
            #print len(hostlist)
            return hostlist

    def hostgroup_get(self, hostgroupName=''): 
        data = json.dumps({ 
                           "jsonrpc":"2.0", 
                           "method":"hostgroup.get", 
                           "params":{ 
                                     "output": "extend", 
                                     "filter": { 
                                                "name": hostgroupName 
                                                } 
                                     }, 
                           "auth":Zabbix_Auth().user_login(), 
                           "id":1, 
                           }) 
         
        request = urllib2.Request(self.url,data) 
        for key in self.header: 
            request.add_header(key, self.header[key]) 
              
        try: 
            result = urllib2.urlopen(request) 
        except URLError as e: 
            print "Error as ", e 
        else: 
            response = json.loads(result.read()) 
            result.close() 


    def template_get(self,templateName=''): 
        data = json.dumps({ 
                           "jsonrpc":"2.0", 
                           "method": "template.get", 
                           "params": { 
                                      "output": "extend", 
                                      "filter": { 
                                                 "name": templateName                                                        
                                                 } 
                                      }, 
                           "auth": Zabbix_Auth().user_login(), 
                           "id":1, 
                           })
         
        request = urllib2.Request(self.url, data) 
        for key in self.header: 
            request.add_header(key, self.header[key]) 
              
        try: 
            result = urllib2.urlopen(request) 
        except URLError as e: 
            print "Error as ", e 
        else: 
            response = json.loads(result.read()) 
            result.close() 

    def hostgroup_create(self,hostgroupName):

        if self.hostgroup_get(hostgroupName):
            print "hostgroup  \033[42m%s\033[0m is exist !"%hostgroupName
            sys.exit(1)
        data = json.dumps({
                          "jsonrpc": "2.0",
                          "method": "hostgroup.create",
                          "params": {
                          "name": hostgroupName
                          },
                          "auth": Zabbix_Auth().user_login(),
                          "id": 1
                          })
        request=urllib2.Request(self.url,data)

        for key in self.header: 
            request.add_header(key, self.header[key]) 
              
        try: 
            result = urllib2.urlopen(request)
        except URLError as e: 
            print "Error as ", e 
        else: 
            response = json.loads(result.read()) 
            result.close()
            print "\033[042m 添加主机组:%s\033[0m  hostgroupID : %s"%(hostgroupName,response['result']['groupids'])


                 
    def host_create(self, hostname, hostip, name, proxyid, hostgroupName, templateName):
        if self.host_get(hostip):
            print "\033[041m该主机已经添加!\033[0m" 
            sys.exit(1)
        group_list=[]
        template_list=[]
        for i in hostgroupName.split(','):
            var = {}
            var['groupid'] = self.hostgroup_get(i)
            group_list.append(var)
        for i in templateName.split(','):
            var={}
            var['templateid']=self.template_get(i)
            template_list.append(var)    

        data = json.dumps({ 
                           "jsonrpc":"2.0", 
                           "method":"host.create", 
                           "params":{ 
                                        "host": name,
                                        "name": hostname, 
                                        "interfaces": [ 
                                                 { 
                                                     "type": 1, 
                                                     "main": 1, 
                                                     "useip": 1, 
                                                     "ip": hostip, 
                                                     "dns": "", 
                                                     "port": "10050" 
                                                  } 
                                        ], 
                                        "groups": group_list,
                                        "templates": template_list,
                                        "proxy_hostid": proxyid,
                                     }, 
                           "auth": Zabbix_Auth().user_login(), 
                           "id":1                   
        }) 
        request = urllib2.Request(self.url, data) 
        for key in self.header: 
            request.add_header(key, self.header[key]) 
              
        try: 
            result = urllib2.urlopen(request) 
        except URLError as e: 
            print "Error as ", e 
        else: 
            response = json.loads(result.read()) 
            result.close() 
            print "添加主机 : \033[32m%s\033[0m \tid :\033[31m%s\033[0m \tproxy :\033[31m%s\033[0m" % (hostip, response, proxyid) 

    def host_disable(self,hostip):
        data=json.dumps({
                        "jsonrpc": "2.0",
                        "method": "host.update",
                        "params": {
                        "hostid": self.host_get(hostip),
                        "status": 1
                        },
                        "auth": Zabbix_Auth().user_login(),
                        "id": 1
        })
        request = urllib2.Request(self.url,data)
        for key in self.header:
            request.add_header(key, self.header[key])         
        try: 
            result = urllib2.urlopen(request)
        except URLError as e: 
            print "Error as ", e 
        else: 
            response = json.loads(result.read()) 
            result.close()
            print self.host_get(hostip)
                 

    def host_delete(self,hostid):
        hostid_list=[]
        for i in hostid.split(','):
            var = {}
            var['hostid'] = self.host_get(i)
            hostid_list.append(var)         
        data=json.dumps({
                        "jsonrpc": "2.0",
                        "method": "host.delete",
                        "params": hostid_list,
                        "auth": Zabbix_Auth().user_login(),
                        "id": 1
                })

        request = urllib2.Request(self.url,data) 
        for key in self.header: 
            request.add_header(key, self.header[key]) 
             
        try: 
            result = urllib2.urlopen(request) 
        except Exception,e: 
            print  e
        else: 
            result.close() 

    def get_host(self, hostip=""):
        data = json.dumps({
            "jsonrpc":"2.0",
            "method":"host.get",
            "params":{
                "output":"extend",
                "filter":{
                    "host":hostip
                    }
                },
            "auth": Zabbix_Auth().user_login(),
            "id":2
            });
        request = urllib2.Request(self.url, data) 
        for key in self.header: 
            request.add_header(key, self.header[key]) 
        try: 
            result = urllib2.urlopen(request) 
        except URLError as e: 
            if hasattr(e, 'reason'):
                print "We failed to reach a server."
                print "reason:", e.reason
            elif hasattr(e, "code"):
                print 'The server could not fulfill the request.' 
                print 'Error code: ', e.code
                return 0
        else:
            response = json.loads(result.read()) 
            result.close() 
            hostsid = []
            for host in response['result']:
                hostsid.append({host['host']:host['hostid']})
            return hostsid

    def get_hostgroup(self, hostgroupname=""):
        data = json.dumps({
                   "jsonrpc":"2.0",
                   "method":"hostgroup.get",
                   "params":{
                             "output": "extend",
                             "filter": {
                                        "name": hostgroupname
                                        }
                             },
                   "auth":Zabbix_Auth().user_login(),
                   "id":1,
                   })
        request = urllib2.Request(self.url,data)
        for key in self.header:
            request.add_header(key, self.header[key])

        try:
            result = urllib2.urlopen(request)
        except URLError as e:
            print "Error as ", e
        else:
            response = json.loads(result.read())
            result.close()
            grouphosts = []
            for group in response['result']:
                grouphosts.append({group['name']:group['groupid']})
            return grouphosts
        
    def get_host_graph(self, hostname):
        data = json.dumps({
                            "jsonrpc": "2.0",
                            "method": "host.get",
                            "params": { "selectGraphs": ["graphid","name"],
                                        "filter": {"host": hostname}},
                            "auth": Zabbix_Auth().user_login(),
                            "id": 1})
        request = urllib2.Request(self.url, data) 
        for key in self.header: 
            request.add_header(key, self.header[key]) 
        try: 
            result = urllib2.urlopen(request) 
        except URLError as e: 
            if hasattr(e, 'reason'):
                print "We failed to reach a server."
                print "reason:", e.reason
            elif hasattr(e, "code"):
                print 'The server could not fulfill the request.' 
                print 'Error code: ', e.code
                return 0
        else:
            response = json.loads(result.read()) 
            result.close() 
            return response['result'][0]['graphs']

    #def get_host_item(self, hostname=""):
    def get_host_item(self, hostid=""):
        data = json.dumps({
            "jsonrpc": "2.0",
            "method": "item.get",
            "params": {
                "output": "extend",
                "hostids": hostid,
                #"host": hostname,
                #"search": {
                #    "key_": "system"
                #},
                #"sortfield": "name"
            },
            "auth": Zabbix_Auth().user_login(),
            "id": 1
        })
        request = urllib2.Request(self.url,data)
        for key in self.header:
            request.add_header(key,self.header[key])
        # get host list
        try:
            result = urllib2.urlopen(request)
        except URLError as e:
            if hasattr(e, 'reason'):
                print 'We failed to reach a server.'
                print 'Reason: ', e.reason
            elif hasattr(e, 'code'):
                print 'The server could not fulfill the request.'
                print 'Error code: ', e.code
        else:
            response = json.loads(result.read())
            result.close()
            print "Number Of host items: ", len(response['result'])
            item_host = []
            for item in response['result']:
                print item
                item_host.append({item["name"]:item["itemid"]})
                #print "Host ID:",host['hostid'],"HostName:",host['name']
            return item_host
    
    def get_host_from_groupid(self, groupid=""):
        data = json.dumps({
           "jsonrpc":"2.0",
           "method":"host.get",
           "params":{
               "output":["hostid","name"],
               "groupids":groupid,
           },
            "auth": Zabbix_Auth().user_login(),
           "id":1,
        })
        request = urllib2.Request(self.url,data)
        for key in self.header:
            request.add_header(key,self.header[key])
        # get host list
        try:
            result = urllib2.urlopen(request)
        except URLError as e:
            if hasattr(e, 'reason'):
                print 'We failed to reach a server.'
                print 'Reason: ', e.reason
            elif hasattr(e, 'code'):
                print 'The server could not fulfill the request.'
                print 'Error code: ', e.code
        else:
            response = json.loads(result.read())
            result.close()
            print "Number Of Hosts: ", len(response['result'])
            group_host = []
            for host in response['result']:
                group_host.append({host["name"]:host["hostid"]})
                #print "Host ID:",host['hostid'],"HostName:",host['name']
            return group_host
       
    def get_items_history(self, itemsid=""):
        data = json.dumps({
            "jsonrpc": "2.0",
            "method": "history.get",
            "params": {
                "output": "extend",
                "history": 0,
                "itemids": itemsid,
                "sortfield": "clock",
                "sortorder": "DESC",
                "limit": 1
            },
            "auth": Zabbix_Auth().user_login(),
            "id": 1
        });
        request = urllib2.Request(self.url, data)
        for key in self.header:
            request.add_header(key, self.header[key])
        try:
            result = urllib2.urlopen(request)
        except URLError as e:
            if hasattr(e, 'reason'):
                print 'We failed to reach a server.'
                print 'Reason: ', e.reason
            elif hasattr(e, 'code'):
                print 'The server could not fulfill the request.'
                print 'Error code: ', e.code
        else:
            response = json.loads(result.read())
            result.close()
            print "Number Of items: ", len(response['result'])
            items_value = []
            for value in response['result']:
                items_value.append({u'itemid':value["itemid"], u'value':value["value"]})
            return items_value
       
    
    def get_graph_value(self, graphid):
        data = json.dumps({
                            "jsonrpc": "2.0",
                            "method": "host.get",
                            "params": { "selectItems": ["itemid"],
                                        "filter": {"graph": graphid}},
                            "auth": Zabbix_Auth().user_login(),
                            "id": 1
                            }
                          )
        request = urllib2.Request(self.url, data) 
        for key in self.header: 
            request.add_header(key, self.header[key]) 
        try: 
            result = urllib2.urlopen(request) 
        except URLError as e: 
            if hasattr(e, 'reason'):
                print "We failed to reach a server."
                print "reason:", e.reason
            elif hasattr(e, "code"):
                print 'The server could not fulfill the request.' 
                print 'Error code: ', e.code
                return 0
        else:
            response = json.loads(result.read()) 
            result.close() 
            tmp = response['result'][0]['items']
            items = []
            for value in tmp:
                print value
            return "test"
        
zabbix_tool = Zabbix_Utils()

#print zabbix_tool.get_hostgroup()
#print zabbix_tool.get_host_from_groupid(537)
#[{u'sjhl-wn-wapesf02v_44.144': u'15515'}, {u'sjhl-wn-wapesf01v_44.145': u'15553'}]
#print zabbix_tool.get_host_graph("sjhl-wn-wapesf02v")
#[{u'graphid': u'64667', u'name': u'Swap usage'}, {u'graphid': u'64668', u'name': u'Memory usage'}, {u'graphid': u'64671', u'name': u'Network traffic on eth0'}, {u'graphid': u'64672', u'name': u'Network traffic on eth1'}, {u'graphid': u'64673', u'name': u'CPU jumps'}, {u'graphid': u'64674', u'name': u'CPU load'}, {u'graphid': u'64675', u'name': u'CPU utilization'}, {u'graphid': u'64676', u'name': u'Nginx Stat'}, {u'graphid': u'69218', u'name': u'IO util on sda'}, {u'graphid': u'69219', u'name': u'IO util on sdb'}, {u'graphid': u'69335', u'name': u'Disk space usage /'}, {u'graphid': u'69336', u'name': u'Disk space usage /www'}, {u'graphid': u'69337', u'name': u'Disk space usage /var'}, {u'graphid': u'69338', u'name': u'Disk space usage /usr'}, {u'graphid': u'69339', u'name': u'Disk space usage /boot'}]
#print zabbix_tool.get_host_item("sjhl-wn-wapesf02v")
#[{u'Context switches per second': u'256012'}, {u'CPU $2 time': u'256013'}, {u'CPU $2 time': u'256014'}, {u'CPU $2 time': u'256015'}, {u'CPU $2 time': u'256016'}, {u'CPU $2 time': u'256017'}, {u'CPU $2 time': u'256018'}, {u'CPU $2 time': u'256019'}, {u'CPU $2 time': u'256020'}, {u'Free swap space': u'255986'}, {u'Free swap space in %': u'255987'}, {u'Host boot time': u'255983'}, {u'Host local time': u'255985'}, {u'Host name': u'255984'}, {u'Interrupts per second': u'256008'}, {u'Processor load (1 min average)': u'256010'}, {u'Processor load (15 min average)': u'256009'}, {u'Processor load (5 min average)': u'256011'}, {u'System information': u'255989'}, {u'System uptime': u'255990'}, {u'Total swap space': u'255988'}]

#print zabbix_tool.get_host_item(16940)
#[{u'Host name of zabbix_agentd running': u'255980'}, {u'Agent ping': u'255981'}, {u'Version of zabbix_agent(d) running': u'255982'}, {u'IO Util on $1': u'274963'}, {u'IO Util on $1': u'274964'}, {u'Incoming network traffic on eth0': u'256002'}, {u'Incoming network traffic on eth1': u'256003'}, {u'Outgoing network traffic on eth0': u'256004'}, {u'Outgoing network traffic on eth1': u'256005'}, {u'Total network traffic on eth0': u'256006'}, {u'Total network traffic on eth1': u'256007'}, {u'Nginx Stat Active': u'256021'}, {u'Nginx Stat Reading': u'256022'}, {u'Nginx Stat Waiting': u'256023'}, {u'Nginx Stat Writing': u'256024'}, {u'Host boot time': u'255983'}, {u'Interrupts per second': u'256008'}, {u'Processor load (15 min average)': u'256009'}, {u'Processor load (1 min average)': u'256010'}, {u'Processor load (5 min average)': u'256011'}, {u'Context switches per second': u'256012'}, {u'CPU $2 time': u'256013'}, {u'CPU $2 time': u'256014'}, {u'CPU $2 time': u'256015'}, {u'CPU $2 time': u'256016'}, {u'CPU $2 time': u'256017'}, {u'CPU $2 time': u'256018'}, {u'CPU $2 time': u'256019'}, {u'CPU $2 time': u'256020'}, {u'Host name': u'255984'}, {u'Host local time': u'255985'}, {u'Free swap space': u'255986'}, {u'Free swap space in %': u'255987'}, {u'Total swap space': u'255988'}, {u'System information': u'255989'}, {u'System uptime': u'255990'}, {u'Free inodes on $1 (percentage)': u'275434'}, {u'Free inodes on $1 (percentage)': u'275438'}, {u'Free inodes on $1 (percentage)': u'275437'}, {u'Free inodes on $1 (percentage)': u'275436'}, {u'Free inodes on $1 (percentage)': u'275435'}, {u'Free disk space on $1': u'275439'}, {u'Free disk space on $1 (percentage)': u'275444'}, {u'Total disk space on $1': u'275449'}, {u'Used disk space on $1': u'275454'}, {u'Free disk space on $1': u'275443'}, {u'Free disk space on $1 (percentage)': u'275448'}, {u'Total disk space on $1': u'275453'}, {u'Used disk space on $1': u'275458'}, {u'Free disk space on $1': u'275442'}, {u'Free disk space on $1 (percentage)': u'275447'}, {u'Total disk space on $1': u'275452'}, {u'Used disk space on $1': u'275457'}, {u'Free disk space on $1': u'275441'}, {u'Free disk space on $1 (percentage)': u'275446'}, {u'Total disk space on $1': u'275451'}, {u'Used disk space on $1': u'275456'}, {u'Free disk space on $1': u'275440'}, {u'Free disk space on $1 (percentage)': u'275445'}, {u'Total disk space on $1': u'275450'}, {u'Used disk space on $1': u'275455'}, {u'Available memory': u'255991'}, {u'Total memory': u'255992'}]


print zabbix_tool.get_items_history(400048)



