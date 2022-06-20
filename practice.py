hello = lambda: print('Hello World!');
pack = lambda a,b,c: [a,b,c];
def eat_lunch(list):
    print('First I eat {first_item}'.format(first_item = list[0]));
    for i in list[1::]: print('Next I eat {next_item}'.format(next_item = i));
    print('My lunchbox is empty');

hello();
lunch = pack('Milk', 'Sandwich', 'Yogurt');
eat_lunch(lunch);