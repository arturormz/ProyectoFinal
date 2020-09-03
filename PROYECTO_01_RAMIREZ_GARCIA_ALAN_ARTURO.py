from lifestore_file import lifestore_products
from lifestore_file import lifestore_sales
from lifestore_file import lifestore_searches
"""
This is the LifeStore-SalesList data:

lifestore-searches = [id_search, id product]
lifestore-sales = [id_sale, id_product, score (from 1 to 5), date, refund (1 for true or 0 to false)]
lifestore-products = [id_product, name, price, category, stock]
"""
Administradores= [["Arturo",240197]]
Admin=[]
for usuario_1 in Administradores:
  Admin.append(usuario_1[0])
Contra_Adm=[]
for usuario_1 in Administradores:
  Contra_Adm.append(usuario_1[1])

Empleados= [["Juan",1234], ["Jaime",4567], ["Sara",6789]]
Emple=[]
for usuario_2 in Empleados:
  Emple.append(usuario_2[0])
Contra_Emp=[]
for usuario_2 in Empleados:
  Contra_Emp.append(usuario_2[1])

Menu_1=[1]
Menu_2=[2]
Menu_3=[3]

Sales=[]
for id_pd in lifestore_sales:
  Sales.append(id_pd[1])

[[x,Sales.count(x)] for x in set(Sales)]
nueva_Sales=(dict((x,Sales.count(x))for x in set (Sales)))
import operator
nueva_Sales_sort = sorted(nueva_Sales.items(), key=operator.itemgetter(1), reverse=True)

No_Venidos=[]
for id_pd in lifestore_products:
  No_Venidos.append(id_pd[0])

diferencia= list(set(No_Venidos) - set(Sales))

Search=[]
for id_sch in lifestore_searches:
  Search.append(id_sch[1])

[[x,Search.count(x)] for x in set(Search)]
nueva_Search=(dict((x,Search.count(x))for x in set (Search)))

import operator
nueva_Search_sort = sorted(nueva_Search.items(), key=operator.itemgetter(1), reverse=True)

diferencia_2= list(set(No_Venidos) - set(Search))

Scores=[]
for id_scr in lifestore_sales:
  Scores.append(id_scr[2])

Nueva_Lista_Scores= list(zip(Sales, Scores))

[[x,Nueva_Lista_Scores.count(x)] for x in set(Nueva_Lista_Scores)]
nueva_Scores=(dict((x,Nueva_Lista_Scores.count(x))for x in set (Nueva_Lista_Scores)))

import operator
nueva_Scores_sort = sorted(nueva_Scores.items(), key=operator.itemgetter(1), reverse= True)

Prices=[]
for id_price in lifestore_products:
  Prices.append (id_price [2])

Dates=[]
for id_date in lifestore_sales:
  Dates.append (id_date[3][3:5])

dic = {1:3019,2:182,3:3089,4:295,5:1779,6:11809,7:8559,8:5399,9:2549,10:889,11:7399,12:6619,13:3989,14:1439,15:8439,16:9799,17:4199,18:2199,19:4509,20:11509,21:5159,22:3429,23:909,24:30449,25:5529,26:1249,27:2109,28:9579,29:2499,30:4029,31:2229,33:4269,40:17439,42:1779,44:2759,45:2869,46:1539,47:1209,48:2559,49:3139,50:2949,51:2399,52:5659,54:259,57:889,60:2519,66:8049,67:3229,74:4239,84:1089,85:2159,89:859,94:2869}

ventas_list=([dic.get(n, n) for n in Sales])

Nueva_Lista_Dates= list(zip(Dates, ventas_list))

def sumar(ventas_list):
  suma=0
  for elemento_vta in ventas_list:
    suma+= elemento_vta
  return suma

[[x,Nueva_Lista_Dates.count(x)] for x in set(Nueva_Lista_Dates)]
nueva_lis_d=(dict((x,Nueva_Lista_Dates.count(x))for x in set (Nueva_Lista_Dates)))

import operator
nueva_Dates_sort = sorted(nueva_lis_d.items(), key=operator.itemgetter(0), reverse=False)

Ventas_mn=[["Ene",104527],["Feb",100171],["Mar",148820],["Abr",168585],["May",88340],["Jun",29094],["Jul",26949],["Ago",3077],["Sep",4199],["Nov",182]]

print("***BIENVENIDO A LIFESTORE***")
print("-----------------------------------------------------------")
usuario= input("Ingresa el nombre del Usuario LIFESTORE: ")
if usuario in Admin:
 print("-Bienvenido Administrador Arturo¡")
 contraseña_1= int(input("Ingresa tu contraseña "+ usuario+":"))
 if contraseña_1 in Contra_Adm:
   print("-Contraseña Correcta :D, AHORA ESTAS DENTRO DE LIFESTORE")
   print("----------------------------------------------------------")
   print("""Menú:
   1-Productos más venidos y más rezagados.
   2-Prductos por reseña en el servicio.
   3-Informacion financiera""")
   seleccion= int(input("Selecciona una opcion del menú (1/2/3):"))
   if seleccion in Menu_1:    
     print ("Selecciono la Opción 1 (Productos más venidos y más rezagados) ")
     print ("--------------------------------------------------")
     print("Los productos más vendidos son:")
     for producto in enumerate(nueva_Sales_sort):
        print("Producto con id:", producto[1][0], "se ha vendido un total de: ", nueva_Sales[producto[1][0]], "Unidades")
     print ("-----------------------------------------------------")
     print ("Los Productos más buscados son:")  
     for busqueda in enumerate(nueva_Search_sort):
       print("Producto con id:", busqueda[1][0], "se ha buscado un total de: ", nueva_Search[busqueda[1][0]], "Veces") 
     print ("-----------------------------------------------------")
     print ("Los Productos menos vendidos son:")
     for No_ven in (diferencia):
        print("Producto con id:", No_ven, "se ha vendido un total de: 0 Unidades")
     print("-----------------------------------------------------")
     print ("Los Productos menos buscados son:")
     for No_serch in (diferencia_2):
        print("Producto con id:", No_serch, "se ha buscado un total de: 0 veces")
   elif seleccion in Menu_2:
     print ("Selecciono la Opción 2 (Productos por reseña en el servicio)")
     print("--------------------------------------------------------")
     print ("Los productos mejor calificados por su reseña son:")
     for score in enumerate(nueva_Scores_sort):
        print("Producto con id:", score[1][0][0], "se ha calificado con:",score[1][0][1], "estrellas", nueva_Scores[score[1][0]], "Veces")
   elif seleccion in Menu_3:
     print ("Selecciono la Opción 3 (Informacion Financiera)")
     print ("-------------------------------------------------------")
     ventas_list=([dic.get(n, n) for n in Sales])
     def sumar(ventas_list):
       suma=0
       for elemento_vta in ventas_list:
         suma+= elemento_vta
       return suma
     print("El total de Ventas Anuales YTD fue de :$",(sumar(ventas_list)))
     print("Las Ventas Promedio por mes son de:$",(sumar(ventas_list))/12)
     for mes in Ventas_mn:
        print ("Las ventas del mes", mes[0],"fue de: $", mes [1])
     for dte in enumerate(nueva_Dates_sort):
        print("Producto con precio de: $", dte[1][0][1], "se ha vendido un total de: ", nueva_lis_d[dte[1][0]], "Veces en el mes", dte[1][0][0], )
        print("$",nueva_lis_d[dte[1][0]]*dte[1][0][1])
   else:
     print ("Opcion incorrecta, intentalo nuevamente")  
 else:
   print("-Contraseña Incorrecta")
elif usuario in Emple:
  print ("-Bienvenido Empleado: "+ usuario)
  contraseña_2= int(input("Ingresa tu contraseña "+ usuario+":"))
  if usuario=="Juan" and contraseña_2==1234:
    print("-Contraseña Correcta :D, AHORA ESTAS DENTRO DE LIFESTORE")
    print("--------------------------------------------------------")
    print("""Menú:
    1-Productos más venidos y más rezagados.
    2-Prductos por reseña en el servicio.
    3-Informacion financiera""")
    seleccion= int(input("Selecciona una opcion del menú (1/2/3):"))
    if seleccion in Menu_1: 
      print ("Selecciono la Opción 1 (Productos más venidos y más rezagados) ")
      print ("--------------------------------------------------")
      print("Los productos más vendidos son:")
      for producto in enumerate(nueva_Sales_sort):
       print("Producto con id:", producto[1][0], "se ha vendido un total de: ", nueva_Sales[producto[1][0]], "Unidades")
      print ("-----------------------------------------------------")
      print ("Los Productos más buscados son:")  
      for busqueda in enumerate(nueva_Search_sort):
       print("Producto con id:", busqueda[1][0], "se ha buscado un total de: ", nueva_Search[busqueda[1][0]], "Veces") 
      print ("-----------------------------------------------------")
      print ("Los Productos menos vendidos son:")
      for No_ven in (diferencia):
        print("Producto con id:", No_ven, "se ha vendido un total de: 0 Unidades")
      print("-----------------------------------------------------")
      print ("Los Productos menos buscados son:")
      for No_serch in (diferencia_2):
        print("Producto con id:", No_serch, "se ha buscado un total de: 0 veces")
    elif seleccion in Menu_2:
     print ("Selecciono la Opción 2 (Productos por reseña en el servicio)")
     print("---------------------------------------------------")
     print ("Los productos mejor calificados por su reseña son:")
     for score in enumerate(nueva_Scores_sort):
        print("Producto con id:", score[1][0][0], "se ha calificado con:",score[1][0][1], "estrellas", nueva_Scores[score[1][0]], "Veces")
    elif seleccion in Menu_3:
     print ("Selecciono la Opción 3 (Informacion Financiera)")
     print ("----------------------------------------------------")
     ventas_list=([dic.get(n, n) for n in Sales])
     def sumar(ventas_list):
       suma=0
       for elemento_vta in ventas_list:
         suma+= elemento_vta
       return suma
     print("El total de Ventas Anuales YTD fue de :$",(sumar(ventas_list)))
     print("Las Ventas Promedio por mes son de:$",(sumar(ventas_list))/12)
     for mes in Ventas_mn:
        print ("Las ventas del mes", mes[0],"fue de: $", mes [1])
     for dte in enumerate(nueva_Dates_sort):
        print("Producto con precio de: $", dte[1][0][1], "se ha vendido un total de: ", nueva_lis_d[dte[1][0]], "Veces en el mes", dte[1][0][0], )
        print("$",nueva_lis_d[dte[1][0]]*dte[1][0][1])
  elif usuario=="Jaime" and contraseña_2==4567:
    print("-Contraseña Correcta :D, AHORA ESTAS DENTRO DE LIFESTORE")
    print("--------------------------------------------------------")
    print("""Menú:
    1-Productos más venidos y más rezagados.
    2-Prductos por reseña en el servicio.
    3-Informacion financiera""")
    seleccion= int(input("Selecciona una opcion del menú (1/2/3):"))
    if seleccion in Menu_1:
      print ("Selecciono la Opción 1 (Productos más venidos y más rezagados) ")
      print ("--------------------------------------------------")
      print("Los productos más vendidos son:")
      for producto in enumerate(nueva_Sales_sort):
       print("Producto con id:", producto[1][0], "se ha vendido un total de: ", nueva_Sales[producto[1][0]], "Unidades")
      print ("-----------------------------------------------------")
      print ("Los Productos más buscados son:")  
      for busqueda in enumerate(nueva_Search_sort):
       print("Producto con id:", busqueda[1][0], "se ha buscado un total de: ", nueva_Search[busqueda[1][0]], "Veces") 
      print ("-----------------------------------------------------")
      print ("Los Productos menos vendidos son:")
      for No_ven in (diferencia):
        print("Producto con id:", No_ven, "se ha vendido un total de: 0 Unidades")
      print("-----------------------------------------------------")
      print ("Los Productos menos buscados son:")
      for No_serch in (diferencia_2):
        print("Producto con id:", No_serch, "se ha buscado un total de: 0 veces")
    elif seleccion in Menu_2:
     print ("Selecciono la Opción 2 (Productos por reseña en el servicio)")
     print("---------------------------------------------------")
     print ("Los productos mejor calificados por su reseña son:")
     for score in enumerate(nueva_Scores_sort):
        print("Producto con id:", score[1][0][0], "se ha calificado con:",score[1][0][1], "estrellas", nueva_Scores[score[1][0]], "Veces") 
    elif seleccion in Menu_3:
     print ("Selecciono la Opción 3 (Informacion Financiera)")
     print ("----------------------------------------------------")
     ventas_list=([dic.get(n, n) for n in Sales])
     def sumar(ventas_list):
       suma=0
       for elemento_vta in ventas_list:
         suma+= elemento_vta
       return suma
     print("El total de Ventas Anuales YTD fue de :$",(sumar(ventas_list)))
     print("Las Ventas Promedio por mes son de:$",(sumar(ventas_list))/12)
     for mes in Ventas_mn:
        print ("Las ventas del mes", mes[0],"fue de: $", mes [1])
     for dte in enumerate(nueva_Dates_sort):
        print("Producto con precio de: $", dte[1][0][1], "se ha vendido un total de: ", nueva_lis_d[dte[1][0]], "Veces en el mes", dte[1][0][0], )
        print("$",nueva_lis_d[dte[1][0]]*dte[1][0][1])
  elif usuario=="Sara" and contraseña_2==6789:
    print("-Contraseña Correcta :D, AHORA ESTAS DENTRO DE LIFESTORE")
    print("--------------------------------------------------------")
    print("""Menú:
    1-Productos más venidos y más rezagados.
    2-Prductos por reseña en el servicio.
    3-Informacion financiera""")
    seleccion= int(input("Selecciona una opcion del menú (1/2/3):"))
    if seleccion in Menu_1:
      print ("Selecciono la Opción 1 (Productos más venidos y más rezagados) ")
      print ("--------------------------------------------------")
      print("Los productos más vendidos son:")
      for producto in enumerate(nueva_Sales_sort):
       print("Producto con id:", producto[1][0], "se ha vendido un total de: ", nueva_Sales[producto[1][0]], "Unidades")
      print ("-----------------------------------------------------")
      print ("Los Productos más buscados son:")  
      for busqueda in enumerate(nueva_Search_sort):
       print("Producto con id:", busqueda[1][0], "se ha buscado un total de: ", nueva_Search[busqueda[1][0]], "Veces") 
      print ("-----------------------------------------------------")
      print ("Los Productos menos vendidos son:")
      for No_ven in (diferencia):
        print("Producto con id:", No_ven, "se ha vendido un total de: 0 Unidades")
      print("-----------------------------------------------------")
      print ("Los Productos menos buscados son:")
      for No_serch in (diferencia_2):
        print("Producto con id:", No_serch, "se ha buscado un total de: 0 veces")
    elif seleccion in Menu_2:
     print ("Selecciono la Opción 2 (Productos por reseña en el servicio)")
     print("---------------------------------------------------")
     print ("Los productos mejor calificados por su reseña son:")
     for score in enumerate(nueva_Scores_sort):
        print("Producto con id:", score[1][0][0], "se ha calificado con:",score[1][0][1], "estrellas", nueva_Scores[score[1][0]], "Veces") 
    elif seleccion in Menu_3:
     print ("Selecciono la Opción 3 (Informacion Financiera)")
     print ("----------------------------------------------------")
     ventas_list=([dic.get(n, n) for n in Sales])
     def sumar(ventas_list):
       suma=0
       for elemento_vta in ventas_list:
         suma+= elemento_vta
       return suma
     print("El total de Ventas Anuales YTD fue de :$",(sumar(ventas_list)))
     print("Las Ventas Promedio por mes son de:$",(sumar(ventas_list))/12)
     for mes in Ventas_mn:
        print ("Las ventas del mes", mes[0],"fue de: $", mes [1])
     for dte in enumerate(nueva_Dates_sort):
        print("Producto con precio de: $", dte[1][0][1], "se ha vendido un total de: ", nueva_lis_d[dte[1][0]], "Veces en el mes", dte[1][0][0], )
        print("$",nueva_lis_d[dte[1][0]]*dte[1][0][1])      
  else:
    print("-Contraseña Incorrecta")
else:
 print("-No coincide, ingrese nuevamente usuario")
