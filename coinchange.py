
'''
Created on Mon Aug 26 19:54:10 2019

@author: MJose

Solution derived from here: https://en.wikipedia.org/wiki/Change-making_problem
Solution source code from: https://bitbucket.org/trebsirk/algorithms/src/master/coinchanging.py
YouTube video of the explanation: https://www.youtube.com/watch?v=EScqJEEKC10

'''

def change(n, coins_available, coins_so_far):
    """

    An implementation of the bakery packing algorithm/coin changing algorithm 
    using dynamic programming.

    This method generates all the possible set that can be produced 
    using the elements in coins_available and will return the set 
    if it sums to n.

    Running this requires that the elements in coins_available are in ascending 
    order to be able to come up with the optimal set (coins_so_far).

    """

    # Check if the coins in coins_so_far sums to n
    if sum(coins_so_far) == n:
        yield coins_so_far
    elif sum(coins_so_far) > n:
        pass
    elif coins_available == []:
        pass
    else:
        # Retrieve another coin (element) in coins_available
        for c in change(n, coins_available[:], coins_so_far + [coins_available[0]]):
            yield c
        for c in change(n, coins_available[1:], coins_so_far):
            yield c

def generate_data(product):
    """
    
    Imports the bakery data and puts it into a Pandas DataFrame.

    Input:
    The product code ('VS5'/'MB11'/'CF') to only yield data related to a specific product.
    Else an empty string ('') to return all data.

    Output:
    The DataFrame with all the requested product code.

    Note:
    This DataFrame contains a Quantity column which will be populated after 
    the bakery packing algorithm has been called.

    """
    import pandas as pd
    
    # Generate data
    df = pd.DataFrame([('Vegemite Scroll', 'VS5', 3, 6.99, 0),
                       ('Vegemite Scroll', 'VS5', 5, 8.99, 0),
                       ('Blueberry Muffin', 'MB11', 2, 9.95, 0),
                       ('Blueberry Muffin', 'MB11', 5, 16.95, 0),
                       ('Blueberry Muffin', 'MB11', 8, 24.95, 0),
                       ('Croissant', 'CF', 3, 5.95, 0),
                       ('Croissant', 'CF', 5, 9.95, 0),
                       ('Croissant', 'CF', 9, 16.99, 0)], columns=['Name','ProductCode', 'Size', 'Price', 'Quantity'])

    if product != '':
        # Filter with the product code if needed
        return df.loc[df['ProductCode'] == product].copy()
    else:
        return df

def order_product(product_string):
    """
    
    Parses the input string coming from the FLASK app.

    Input:
    According to the specs, the input string should be in the format
    [quantity] [product code]

    Example:
    10 VS5

    Output:
    This will return a default error message ('Invalid input detected. 
    Please try again.') if the string is not in the format above.

    """

    product_string = product_string.split(' ')

    # Parses the input string
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
    """

    Processes the input string and calls the bakery packing algorithm.

    Input:
    n - the quantity of the product
    product - the product code

    Example:
    pack_product(10, 'VS5')

    Output:
    A string that contains the optimal packaging solution.

    '10 VS5 $17.98:\n\t2 x 5 at $8.99\n'


    """

    try:
        # Generate the product dataframe
        df = generate_data(product)
        coins = list(df.loc[df['ProductCode'] == product]['Size'])

        # Call change() which is the bakery packing algorithm
        solutions = [s for s in change(n, coins, [])]

        # Search for the optimal solution by choosing the set with the lowest length
        optimal_solution = min(solutions, key=len)
        
        # Populate the quantity (how many) of each sizes should we pack
        for i in optimal_solution:
            df.loc[(df['Size'] == i),'Quantity'] = df.loc[(df['Size'] == i),'Quantity'] + 1
        
        df = df.iloc[::-1]
        
        # Format the return string
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
     
        
    