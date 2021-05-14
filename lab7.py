#####################################################
# APS106 Winter 2021 - Lab 7 - Chemical Eqn Checker #
#####################################################

######################################################
# PART 1 - Complete the function below to deocompose
#          a compound formula written as a string
#          in a dictionary
######################################################

def mol_form(compound_formula):
    """(str) -> dictionary
    When passed a string of the compound formula, returns a dictionary 
    with the elements as keys and the number of atoms of that element as values.
    
    >>> mol_form("C2H6O1")
    {'C': 2, 'H': 6, 'O': 1}
    >>> mol_form("C1H4")
    {'C': 1, 'H': 4}
    """
    
    Numbers_List = []
    Letters_List = []
    Dict = {}
    
    for i in range(len(compound_formula)):
        if(compound_formula[i].isalpha() == True):
            Letters_List.append(compound_formula[i])
        else:
            Numbers_List.append(int(compound_formula[i]))
    
    
    Letters_List2=[]
    
    for j in range(0,len(Letters_List)):
        if(Letters_List[j].isupper() == True):
            Letters_List2.append(Letters_List[j])
        elif(Letters_List[j].islower() == True):
            Letters_List2[j-1] = Letters_List2[j-1] + Letters_List[j]
    
    
    for k in range(len(Numbers_List)):
        Dict.update({Letters_List2[k]:Numbers_List[k]})
    
    
    return (Dict)
     
    pass # TODO your code here

######################################################
# PART 2 - Complete the function below that takes two 
#          tuples representing one side of a
#          chemical equation and returns a dictionary
#          with the elements as keys and the total
#          number of atoms in the entire expression
#          as values.
######################################################
    
def expr_form(expr_coeffs,expr_molecs):
    """
    (tuple (of ints), tuple (of dictionaries)) -> dictionary
    
    This function accepts two input tuples that represent a chemical expression,
    or one side of a chemical equation. The first tuple contains integers that
    represent the coefficients for molecules within the expression. The second
    tuple contains dictionaries that define these molecules. The molecule
    dictionaries have the form {'atomic symbol' : number of atoms}. The order
    of the coefficients correspond to the order of molecule dictionaries.
    The function creates and returns a dictionary containing all elements within
    the expression as keys and the corresponding number of atoms for each element
    within the expression as values.
    
    For example, consider the expression 2NaCl + H2 + 5NaF
    
    >>> expr_form((2,1,5), ({"Na":1, "Cl":1}, {"H":2}, {"Na":1, "F":1}))
    {'Na': 7, 'Cl': 2, 'H': 2, 'F': 5}
    
    """
    Empty = {}
    for i in range(len(expr_coeffs)):
        for j in expr_molecs[i]:
            expr_molecs[i][j] = expr_coeffs[i] * expr_molecs[i][j]
    
    for k in range(len(expr_molecs)):
        Empty.update(expr_molecs[k])
        
    for m in Empty:
        Empty[m] = 0
    
    for n in range(len(expr_molecs)):
        for p in expr_molecs[n]:
            if p in Empty:
                Empty[p] += expr_molecs[n][p]
    
    return(Empty)    


    pass # TODO your code here

########################################################
# PART 3 - Check if two dictionaries representing
#          the type and number of atoms on two sides of
#          a chemical equation contain different
#          key-value pairs
########################################################

def find_unbalanced_atoms(reactant_atoms, product_atoms):
    """
    (Dict,Dict) -> Set
    
    Determine if reactant_atoms and product_atoms contain equal key-value
    pairs. The keys of both dictionaries are strings representing the 
    chemical abbreviation, the value is an integer representing the number
    of atoms of that element on one side of a chemical equation.
    
    Return a set containing all the elements that are not balanced between
    the two dictionaries.
    
    >>> find_unbalanced_atoms({"H" : 2, "Cl" : 2, "Na" : 2}, {"H" : 2, "Na" : 1, "Cl" : 2})
    {'Na'}
    
    >>> find_unbalanced_atoms({"H" : 2, "Cl" : 2, "Na" : 2}, {"H" : 2, "Na" : 2, "Cl" : 2})
    set()
    
    >>> find_unbalanced_atoms({"H" : 2, "Cl" : 2, "Na" : 2}, {"H" : 2, "F" : 2, "Cl" : 2})
    {'F', 'Na'}
    """
    Set = set()
    for i in product_atoms: 
        if(reactant_atoms.get(i) == None):
            Set.add(i)
        elif (reactant_atoms[i]!=product_atoms[i]):
            Set.add(i)
    
    for i in reactant_atoms: 
        if(product_atoms.get(i) == None):
            Set.add(i)

    return(Set)
    
    pass # TODO your code here


########################################################
# PART 4 - Check if a chemical equation represented by
#          two nested tuples is balanced
########################################################

def check_eqn_balance(reactants,products):
    """
    (tuple,tuple) -> Set
    
    Check if a chemical equation is balanced. Return any unbalanced
    elements in a set.
    
    Both inputs are nested tuples. The first element of each tuple is a tuple
    containing the coefficients for molecules in the reactant or product expression.
    The second element is a tuple containing strings of the molecules within
    the reactant or product expression. The order of the coefficients corresponds
    to the order of the molecules. The function returns a set containing any
    elements that are unbalanced in the equation.
    
    For example, the following balanced equation
    C3H8 + 5O2 <-> 4H2O + 3CO2
    
    would be input as the following two tuples:
    reactants: ((1,5), ("C3H8","O2"))
    products: ((4,3), ("H2O1","C1O2"))
    
    >>> check_eqn_balance(((1,5), ("C3H8","O2")),((4,3), ("H2O1","C1O2")))
    set()
    
    Similarly for the unbalanced equation
    
    C3H8 + 2O2 <-> 4H2O + 3CO2
    
    would be input as the following two tuples:
    reactants: ((1,2), ("C3H8","O2"))
    products: ((4,3), ("H2O1","C1O2"))
    
    >>> check_eqn_balance(((1,2), ("C3H8","O2")),((4,3), ("H2O1","C1O2")))
    {'O'}
    
    """
    T_Reactants_Vals = reactants[0]
    Reactants_List = []
    for i in range(len(reactants[1])):
        Reactants_List.append(mol_form(reactants[1][i]))
     
    Reactants_Tuple = tuple(Reactants_List)
    Reactants_Dict = expr_form(T_Reactants_Vals,Reactants_Tuple)
    
    
    T_Products_Vals = products[0]
    Products_List = []
    for i in range(len(products[1])):
        Products_List.append(mol_form(products[1][i]))
     
    Products_Tuple = tuple(Products_List)
    Products_Dict = expr_form(T_Products_Vals,Products_Tuple)    

    
    Unbalanced_Expression = find_unbalanced_atoms(Reactants_Dict,
                                                  Products_Dict)
                                                  
    return Unbalanced_Expression
        
    
    pass #TODO your code here