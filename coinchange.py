
'''
Created on Mon Aug 26 19:54:10 2019

@author: MJose

Solution derived from here: https://en.wikipedia.org/wiki/Change-making_problem
Solution source code from: https://bitbucket.org/trebsirk/algorithms/src/master/coinchanging.py
YouTube video of the explanation: https://www.youtube.com/watch?v=EScqJEEKC10

'''

def change(n, coins_available, coins_so_far):
	if sum(coins_so_far) == n:
		yield coins_so_far
	elif sum(coins_so_far) > n:
		pass
	elif coins_available == []:
		pass
	else:
		for c in change(n, coins_available[:], coins_so_far + [coins_available[0]]):
			yield c
		for c in change(n, coins_available[1:], coins_so_far):
			yield c

def generate_data(product):
    import pandas as pd
    
    df = pd.DataFrame([('Vegemite Scroll', 'VS5', 3, 6.99, 0),
                       ('Vegemite Scroll', 'VS5', 5, 8.99, 0),
                       ('Blueberry Muffin', 'MB11', 2, 9.95, 0),
                       ('Blueberry Muffin', 'MB11', 5, 16.95, 0),
                       ('Blueberry Muffin', 'MB11', 8, 24.95, 0),
                       ('Croissant', 'CF', 3, 5.95, 0),
                       ('Croissant', 'CF', 5, 9.95, 0),
                       ('Croissant', 'CF', 9, 16.99, 0)], columns=['Name','ProductCode', 'Size', 'Price', 'Quantity'])

    if product != '':
        return df.loc[df['ProductCode'] == product].copy()
    else:
        return df

def order_product(product_string):
    product_string = product_string.split(' ')

    # TODO: check input here
    try:
        n = int(product_string[0])
        product = product_string[1]

        result = pack_product(n, product)

        if result == None:
            return 'Invalid input detected. Please try again.'
        
        return result

    except:
        return 'Invalid input detected. Please try again.'

def pack_product(n, product):
    
    try:
        df = generate_data(product)
        coins = list(df.loc[df['ProductCode'] == product]['Size'])
        solutions = [s for s in change(n, coins, [])]
        optimal_solution = min(solutions, key=len)
        
        for i in optimal_solution:
            df.loc[(df['Size'] == i),'Quantity'] = df.loc[(df['Size'] == i),'Quantity'] + 1
        
        # you may return the dataframe with the quantity here
        # return df
        
        # print the quantity
        # you may put this in another function
        df = df.iloc[::-1]
        
        total = round(sum(df['Price'] * df['Quantity']), 2)
        result = str(n) + ' ' + product + ' $' + str(total) + ':\n'
        
        for index, row in df.iterrows():
            if row['Quantity'] > 0:
                result = result + '\t' + str(row['Quantity']) + ' x ' + str(row['Size']) + ' at $' + str(row['Price']) + '\n'
                
        return result
    except:
        return None
    

if __name__ == '__main__':
	#n = 14
	#coins = [2, 5, 8]
    # optimal solution: [2, 2, 2, 8]

    #n = 10
    #coins = [3, 5]
    # optimal solution: [5, 5]
    
    #n = 13
    #coins = [3, 5, 9]
    # optimal solution: [3, 5, 5]

    pack_product(10, 'VS5')
    pack_product(14, 'MB11')
    pack_product(13, 'CF')
     
        
    