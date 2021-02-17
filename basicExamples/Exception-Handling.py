x = {'Cloud': 'AWS', 'Container': 'Docker'}
try:
    print(x)

except ZeroDivisionError:
    print('Can not divide by 0')
except:
    print('Common Exception')
finally:
    print('Finally all dots will join')
