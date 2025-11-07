class Employee():
    def _int_(self):
        print('employee created')
    def _del_(self):
        print('destroyed')
def Create_obj():
    print('making object....')
    obj = Employee()
    print('function end.....')
    return obj
print('calling create_obj()function....')
obj = Create_obj()
print('program end...')