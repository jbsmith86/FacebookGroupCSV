import simplejson
import csv
import urllib2
import copy

apikey = raw_input("Enter Facebook API key : ")
groupurl = raw_input("Enter Facebook group url i.e. https://graph.facebook.com/XXXXXXXXXXXXX/members : ")
filename = raw_input("Enter a csv filename i.e. fbgroup.csv : ")
fb = urllib2.urlopen(groupurl + "?" + 'access_token=' + apikey + '&fields=first_name%2Clast_name%2Clink%2Cname%2Cmiddle_name%2Cpicture.type%28small%29')
responce = simplejson.loads(fb.read())['data']
fbgrouplist = createfbgrouplist(responce)
fbgrouplist.sort()
writeCSV(fbgrouplist, filename)

class FBGroupMember(object):
    def __init__(self, name, first, last, pic, fbid, url, middle):
        self.name = name
        self.first_name = first
        self.middle_name = middle
        self.last_name = last
        self.picture_url = pic
        self.fbid = fbid
        self.fb_url = url
    def __name__(self):
        return self.name
    def __lt__(self, other):
        return self.name < other.name
    def __repr__(self):
        return self.name


def createfbgrouplist(jsonres):
    list = []
    for i in range(len(jsonres)):
        name = jsonres[i]['name'].encode("utf8")
        first = jsonres[i]['first_name'].encode("utf8")
        last = jsonres[i]['last_name'].encode("utf8")
        pic = jsonres[i]['picture']['data']['url'].encode("utf8")
        fbid = jsonres[i]['id'].encode("utf8")
        url = jsonres[i]['link'].encode("utf8")
        try:
            middle = jsonres[i]['middle_name'].encode("utf8")
        except KeyError:
            middle = ''
        list.append(FBGroupMember(name, first, last, pic, fbid, url, middle))
    return list

def writeCSV(fbgrouplist, filename):
  file_writer = csv.writer(open(filename, 'wb'))
	file_writer.writerow(['Name', 'First Name', 'Middle Name', 'Last Name', 'Facebook URL', 'Picture URL', 'Facebook ID'])
	for j in fbgrouplist:
		row = []
		row.append(j.name)
		row.append(j.first_name)
		if j.middle_name == None:
			row.append('')
		else:
			row.append(j.middle_name)
		row.append(j.last_name)
		row.append(j.fb_url)
		row.append(j.picture_url)
		row.append(j.fbid)
		file_writer.writerow(row)
