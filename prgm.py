date=['01','01','2022']
date_format=['day','month','year']
from string import digits

date_dict={}

def main():
    if len(date)==3:
        for item in range(len(date)):
            if item==0:
                if not set(date[item]).difference(digits):
                    if 0<=int(date[item])<=31:
                        value_update(date_format[item],date[item])
                    else:
                        print('Invalid day')
                else:
                    print('Invalid day')
            elif item==1:
                if not set(date[item]).difference(digits):
                    if 0<=int(date[item])<=12:
                        value_update(date_format[item],date[item])
                    else:
                        print('Invalid month')
                else:
                    print('Invalid month')
            else:
                value_update(date_format[item],date[item])
        print(date_dict)
    else:
        print('Invalid date submission')

def value_update(value1,value2):
    date_dict.update(
        {
            value1:value2
        }        
    )
main()
