#***ERROR***

##**before**
### def get_age(self):
       now = datetime.datetime.now()
       return self.yob - now.year
##**after**
### **def get_age(self):**
    now = datetime.datetime.now()
    return now.year - self.yob

##**before**
### def get_age(self):
       self.address == address
##**after**
### **def set_address(self, address):**
        self.address = address

##**before**
### def is_homeless(self):
       '''
       returns True if address is not set, false in other case
       '''
       return address is None

##**after**
### **def is_homeless(self):**
        if len(self.address) > 1:
            return True
        else:
            return self.address is None