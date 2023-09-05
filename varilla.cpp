//Stefano Herrejon Antuñano, A00571720
//Corte de varilla
#include <string>
#include <iostream>
#include <climits>
using namespace std;


int corte( int precios[],int longitud){
    if(longitud == 0){
        return 0;
    }
     
    int maxValue = INT32_MIN;
    long long costo = 0;

    for (int i = 1; i <= longitud; i++){

        int tmpPrecio = 0;

        if( i-1 <10){
            tmpPrecio = precios[i-1];
        }

        maxValue =  max(tmpPrecio + corte(precios, longitud - i),maxValue);
    }
    //cout<<maxValue<<endl;
    return maxValue;
}


int main(){    
    int precio[]  = {1,5,8,9,10,17,17,20,24,30};   
    int longitud = 20;
    long long resultado = 0;
    resultado = corte(precio,longitud);
    cout<<"Resultado de "<<longitud<<" es = "<<resultado;

    return 0;
}
