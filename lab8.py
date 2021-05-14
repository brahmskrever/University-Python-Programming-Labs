###########################################################
# APS106 Winter 2021 - Lab 8 - Cable Performance Analyzer #
###########################################################

import csv

#########################################################
# PART 0A - The function below computes the 
#           the cost of a cable based on its material
#           and thickness
#########################################################

def cable_cost(material, diameter, material_costs, diameter_fixed_cost, 
               diameter_marginal_cost, diameter_cost_thresh):
    """
    (str, float, dict, float, float, float) -> float
    
    Computes the cost of manufacturing a cable with specified material
    and diameter. The total cost computed by the function is the sum
    of the material cost and the diameter cost. The final result should
    be rounded to the nearest cent (2 decimal places).
    
    The diameter cost consists a fixed price as well as a marginal
    per unit cost for any diameter greater than a specified threshold.
    The marginal cost only applies to any diameter that exceeds a manufacturer
    specific threshold.
    
    Function Inputs
    ---------------
        material               - string specifying the cable material
        diameter               - the diameter of the cable
        material_costs         - dictionary of material costs
        diameter_fixed_cost    - the fixed cost for manufacturing any diameter
        diameter_marginal_cost - the per unit diameter cost for manufacturing
                                 cables above the treshold value
        diameter_cost_thrsh    - the threshold at which the manufacturer will
                                 apply the additional marginal cost
     

    """
    cost = (material_costs[material] + diameter_fixed_cost + 
            max(0,diameter-diameter_cost_thresh)*diameter_marginal_cost)
    
    return round(cost, 2)


##############################################################################
# PART 0B - The function below computes the maximum load per
#           unit cost measure of cable performance
##############################################################################
def cable_strength_per_cost(material, diameter, max_strength, material_costs, 
                            diameter_fixed_cost, diameter_marginal_cost, 
                            diameter_cost_thresh):
    """
    (str, float, float, dict, float, float, float) -> float
    
    Computes the maximum tensile strength per unit cost of a cable with a given material
    and diameter. The function should compute the cost by calling the cable_cost
    function. The final result should be rounded to one decimal place.
    
    Function Inputs
    ---------------
        material               - string specifying the cable material
        diameter               - the diameter of the cable
        max_strength           - the maximum tensile strength of the cable
        material_costs         - dictionary of material costs
        diameter_fixed_cost    - the fixed cost for manufacturing any diameter
        diameter_marginal_cost - the per unit diameter cost for manufacturing
                                 cables above the treshold value
        diameter_cost_thrsh    - the threshold at which the manufacturer will
                                 apply the additional marginal cost
    
    """
    perf = max_strength / cable_cost(material,diameter, material_costs, 
                                     diameter_fixed_cost, diameter_marginal_cost,
                                     diameter_cost_thresh)
    
    return round(perf,1)



#########################################################
# PART 1 - Complete the function below to read in a file
#          containing material names and their associated
#          cost
#########################################################


def parse_material_costs(material_cost_filename):
    """
    (str) -> dict
    
    Function reads a two column csv file containing material names
    in the first column and material costs in the second column
    and returns a dictionary of material-cost key-value pairs.
    The costs should be stored as floats within the dictionary.
    
    The first row of the read file should contain the headers
    'material' and 'cost'. These should not be included in the dictionary.
    
    """
    
    ## TODO your code here
    
    materials_list = []
    materials_dict = {}
    
    with open(material_cost_filename,"r") as file:
        csv_list = csv.reader (file)
        
        for row in csv_list: 
            materials_list.append (row) 


    materials_list.pop(0)
    
    for i in range(len(materials_list)):
        materials_dict.update({materials_list[i][0]: float(materials_list[i][1])})

        
    return (materials_dict)        
    pass


#############################################################
# PART 2 - Complete the function below to parse the test
#          results and return the results within a dictionary
#############################################################

def parse_test_results(test_result_filename):
    """
    (str) -> dict
    
    Function reads cable stress test results and returns nested dictionary
    of max tensile strength values for each cable configuration (material 
    and diameter).
    
    Results are returned as a nested dictionary where max tensile strengths
    are indexed by material and diameter. The outer dictionary uses the
    materials as keys to index to a dictionary of diameter-cable_performance
    key-value pairs.
    
    e.g. return_dict = {'material-X' : {1.0   : 4.9,
                                        10.0  : 15.4,
                                        30.0  : 20.2,
                                        100.0 : 17.3},
                        'material-Y' : {1.0   : 104.9,
                                        10.0  : 115.4,
                                        30.0  : 120.2,
                                        100.0 : 117.3},
                        'material-Z' : {1.0   : 14.9,
                                        10.0  : 25.4,
                                        30.0  : 30.2,
                                        100.0 : 27.3}}
    
    See the lab pdf for details about the csv file
    """

    ## TODO your code here
    Dict = {}
    Final_Dict = {}
    materials_list = []
    List = []
    with open(test_result_filename,"r") as file:
        csv_list = csv.reader (file)
        
        for row in csv_list: 
            materials_list.append (row) 

    for i in range(1,len(materials_list)):
        if(i>1):
            List.append(Dict)
            Dict = {}
        for j in range(1,len(materials_list[0])):
            Dict.update({float(materials_list[0][j]):float(materials_list[i][j])})
    
    Dict = {}
    
    for m in range(1,len(materials_list[0])):
        Dict.update({float(materials_list[0][m]):float(materials_list[-1][m])})
    
    List.append(Dict)
    
    for k in range(1,len(List)+1):
        Final_Dict.update({materials_list[k][0]:List[k-1]})
    
    return(Final_Dict)

    
    pass



#############################################################
# PART 3 - Complete the function below to perform analysis
#          of test data stored within a csv file and 
#          return the best 3 cables
#############################################################

def analyze_test_results(test_result_filename, material_cost_filename,
                         diameter_fixed_cost, diameter_marginal_cost, 
                         diameter_cost_thresh):
    """
    (str, str, float, float, float) -> tuple
    
    Analyzes the test results within test_result_filenme and returns
    a tuple containing the three best cable configurations.
    
    Results are returned as a tuple where each element is a three-element
    tuple containing the material, diameter, and maximum load per unit cost
    for the cable. The tuples of cable information should be stored in order
    from the highest maximum load per unit cost to lowest maximum load per
    unit cost.
    e.g. (('material-X',10.5,55.9), ('material-Y',5.25,45.2), ('material-X',10.0,44.8))
    """
    
    # material_cost_filename-> parse_material_costs -> get costs Dict
    # test_result_filename - > parse_test_results -> get strength dict
    # need diameter for cable_strength_per_cost -> loop through test_results dict
    
    Test_Results_Dict = parse_test_results(test_result_filename)
    Material_Cost_Dict = parse_material_costs(material_cost_filename)
    
    Material_Name = ""
    Diameter = 0
    Strength = 0
    List = []
    Final_List = []
    Tuple_List = []
    
    for i in Test_Results_Dict:
        Material_Name = i
        for j in Test_Results_Dict[i]:
            Diameter = j
            Strength = Test_Results_Dict[i][j]
            List.append([cable_strength_per_cost(Material_Name,Diameter,
                                                Strength, Material_Cost_Dict,
                                                diameter_fixed_cost, diameter_marginal_cost, 
                                                diameter_cost_thresh),Diameter,Material_Name])    
            List.sort()
        
    for k in range(len(List)-1,len(List)-4,-1):
        Final_List.append(List[k])
    
    for h in range(len(Final_List)):
        Final_List[h].reverse()
    
    for b in range(len(Final_List)):
        Tuple_List.append(tuple(Final_List[b]))
    
    
    return tuple(Tuple_List)
                                                    
    
                
            
    
    ## TODO your code here
    pass
