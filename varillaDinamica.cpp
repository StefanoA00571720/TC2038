//Stefano Herrejon Antuñano, A00571720
//Varilla Dinamica
#include <vector>
#include <iostream>
#include <climits>
#include <array>

using namespace std;
//{}
int corte(const std::array<int, 10>& precios,int n, vector <int> &memo){
    if(memo[n] == -1){
        if(n == 0){
            memo[n] = 0;
            return 0;
        }
        
        int maxValue = INT8_MIN;
        long costo = 0;
    

        for (int i = 1; i <= n; i++)
        {
            int tmpPrecio = 0;
            if ((i-1) < precios.size()){
                tmpPrecio = precios[i - 1]; 

            }

            maxValue =  max(tmpPrecio + corte(precios, n - i,memo),maxValue);
            
        }
        //cout<<maxValue<<endl;
        memo[n] = maxValue;
        return maxValue;
    }else{
        return memo[n];
    }

}
    


main(){

    std::array<int, 10> precio  = {1,5,8,9,10,17,17,20,24,30};
    int longitud = 25;

    vector <int> memo{};
    for (int i = 0; i <= longitud; i++) {
        memo.push_back(-1);
    }

    long long resultado = 0;
    resultado = corte(precio,longitud, memo);
    cout<<"Resultado de "<<longitud<<" es = "<<resultado<<endl;

    for(int i = 0;i<=longitud;i++){
        cout<<i<<" "<<memo[i]<<endl;
    }
}
    
