//Stefano Herrejon Antuñano, A00571720
//Lineas más cortas

#include <iostream>
#include <vector>
#include <cmath>
using namespace std;


vector <pair<int,int>> coordenadas = {

       {20, 20}, {20, 40}, {20, 160}, {30, 120}, {40, 140}, 
       {40, 150}, {50, 20}, {60, 40}, {60, 80}, {60, 200}, 
       {70, 200}, {80, 150}, {90, 170}, {90, 170}, {100, 50}, 
       {100, 40}, {100, 130}, {100, 150}, {110, 10}, {110, 70}, 
       {120, 80}, {130, 70}, {130, 170}, {140, 140}, {140, 180}, 
       {150, 50}, {160, 20}, {170, 100}, {180, 70}, {180, 200}, 
       {200, 30}, {200, 70}, {200, 100}

};


vector <bool> boleanos{
    {0},{0},{0},{0},{0},{0},{0},{0},{0},{0},
    {0},{0},{0},{0},{0},{0},{0},{0},{0},{0},
    {0},{0},{0},{0},{0},{0},{0},{0},{0},{0},
    {0},{0},{0}
};

vector <pair<int,int>> respuesta;

int comparar(int comparar){
    float final = 1000; //El resultado de menor distancia hasta el momento, se inicia alto
    float momentaria = 0; //El resultado mometario de la ecuación de distancia
    int elegida = 0; //El vector con menor distancia

    for(int i = 0;i<coordenadas.size();i++){
        if(comparar != i && boleanos[i] == false){
            momentaria = sqrt(pow(coordenadas[i].first-coordenadas[comparar].first,2)+
                            pow(coordenadas[i].second-coordenadas[comparar].second,2));
            if(momentaria < final){
                elegida = i;
                final = momentaria;
            }
        }
    }           

   // cout<<"->"<<coordenadas[comparar].first<<" "<<coordenadas[comparar].second<<endl;
   // cout<<" "<<final<<"->"<<coordenadas[elegida].first<<" "<<coordenadas[elegida].second<<endl;

    boleanos[elegida] = true;
    return elegida;
};


int lineaRecta(int comienzo){
    int vecinoCercano = comienzo;

    boleanos[comienzo] = true;
    respuesta.push_back(coordenadas[comienzo]);


    for(int i = 0; i<coordenadas.size()-1;i++){
        //cout<<"Vecino cercano = "<<vecinoCercano<<endl;
        vecinoCercano = comparar(vecinoCercano);
        //cout<<"Vecino cercano = "<<vecinoCercano<<endl;
        //cout<<endl;

        respuesta.push_back(coordenadas[vecinoCercano]);
    }

    return 0;
};



main (){
    int comienzo = 0; // Del 0 al 32
   // cin>>comienzo;
    int answer = lineaRecta(comienzo);

    for(int i = 0;i<respuesta.size();i++){
        cout<<i<<") "<<respuesta[i].first<<"-"<<respuesta[i].second<<" ->"<<endl;   
    }

}