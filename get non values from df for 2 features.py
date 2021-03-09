def get_notnull_value(df):
    '''This function takes in a dataframe, selects columns that dont contain null values. 
         To get the values, it iterates row-wise to select first valid index i.e. a not-null value. 
         The lists obtained are then written to a dataframe. 
         
         Usage: new_df = get_notnull_value(df) 
         df is your dataframe that contains null values and new_df will contain the non-null values''' 
    
    get_cols = df.apply(pd.Series.first_valid_index, axis=1) 
    get_vals = [df.loc[k,v] if v is not None else None for k, v in get_cols.iteritems()] 
    
    transformed_df = pd.DataFrame({'Provider' : get_cols,
                                   'Values' : get_vals})   
    return transformed_df
