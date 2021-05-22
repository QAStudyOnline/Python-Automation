variable = 9

if variable == 10:
    print('variable equal 10')
elif variable < 10:
    print('variable less then 10')
else:
    print('variable great then 10')

list_to_test = [1, 2, 3]

if list_to_test:
    print("List is not empty")

if len(list_to_test) != 0:
    print("List is not empty")

# in operator
if 10 in [20, 30, 20, 10]:
    print("10 in list")

if 'alpha' in 'alpha omega delta':
    print('alpha in list')


ukraine_city = {
    'kyiv':
        {
            'Area': '839',
            'Population': '2,950,819'
        },
    'rivne':
        {
            'Area': '63.00',
            'Population': '246,003'
        }
}

vlan = [10, 20, 30, 40]

if 10 in vlan and 'kyiv' in ukraine_city:
    print("Bingo")

if 12 in vlan or 'kyiv' in ukraine_city:
    print("Hm.......")


if 12 not in vlan or 'kyiv' in ukraine_city:
    print("success")
