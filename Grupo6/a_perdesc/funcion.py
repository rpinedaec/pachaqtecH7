
# set_up
def set_up_perdesc():
    perdesc_list=[
        {'Año':'2020','Bimestre': 'primer'},
        {'Año':'2020','Bimestre': 'segundo'},
        {'Año':'2020','Bimestre': 'tercer'},
        {'Año':'2020','Bimestre': 'cuarto'}, 
    ]
    return perdesc_list

#  create one
def insert_perdesc(ano,bimestre):
    mydict={'Año':ano,'bimestre':bimestre}
    return mydict
    
# find
def find_perdesc(ano):
    query={'Año':ano}
    return query

# delete
def delete_perdesc(ano,bimestre):
    query={'Año':ano,'bimestre':bimestre}
    return query

# update
def update_perdesc_DNI(DNI):
    query_DNI={"DNI":DNI}
    return query_DNI

def update_perdesc(new_value,new_field):
    perdesc_dict={'$set':{'field':'value'}}
    perdesc_dict['$set']['field']=new_value
    perdesc_dict['$set'][new_field]=perdesc_dict['$set'].pop('field')
    return perdesc_dict


