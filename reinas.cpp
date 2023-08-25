//Stefano Herrejon,Miniconflicts para solución de reinas
#include <iostream>
#include <vector>
using namespace std;
//Pares de vectores

//Vector ya arreglado

/*
vector <pair<int,int>> reinas = {

        {0,2},
        {1,5},
        {2,7},
        {3,1},
        {4,3},
        {5,0},
        {6,6},
        {7,4}

};
*/
   

//Vector con 3 distintos
/*
vector <pair<int,int>> reinas = {

    {0,2},
    {1,1},
    {2,7},
    {3,1},
    {4,3},
    {5,3},
    {6,6},
    {7,2}

 };
*/


//Vector todos en 0
/*  

vector <pair<int,int>> reinas = {

        {0,0},
        {1,0},
        {2,0},
        {3,0},
        {4,0},
        {5,0},
        {6,0},
        {7,0}

         };
*/

//Vector en diagonal
/*
vector <pair<int,int>> reinas = {
        {0,0},
        {1,1},
        {2,2},
        {3,3},
        {4,4},
        {5,5},
        {6,6},
        {7,7}
};
*/


//fila,columna
 //Vector random
 vector <pair<int,int>> reinas = {
        {0,4},
        {1,6},
        {2,1},
        {3,2},
        {4,3},
        {5,2},
        {6,7},
        {7,5}
};
 
//Checa el numero de conflicto checacndo si estan en la misma fila/columna o si estan en diagonal
int numConflictos(int reina){
    int conflicts = 0;
    for(int i = 0;i<=7;i++){
        if(reina != i){
            if(reinas[reina].first == reinas[i].first || reinas[reina].second == reinas[i].second){
                conflicts ++;
            }
            if(abs(reinas[reina].first - reinas[i].first) == abs(reinas[reina].second - reinas[i].second)){
                conflicts ++;
            }
        }
    }
    return conflicts;
};


int minConflicts(int repeticion){
    int reinaActual = 0;
    int reinaPasada = 8;
 


    for(int i = 0;i<repeticion;i++){
        int conflicts = 0;
        int numConf = 0;
        int numConfAlto = 0; 


        for(int z = 0;z<=7;z++){

            numConf = numConflictos(z);

            if(numConf >= numConfAlto && z != reinaPasada){
                reinaActual = z;
                numConfAlto = numConf;
            }

        }

        for(int y = 0;y<8;y++){
            conflicts += numConflictos(y);

        }

        if(conflicts == 0){
            cout<<"Ya no hay conflictos "<<endl;
            return 1;

            break;
        }

        
        int numConfActual = conflicts;
        int columna = 0;
        int conflictos = 0;

            for(int x = 0;x<=7;x++){

                reinas[reinaActual].second = reinas[reinaActual].second+1;
                if(reinas[reinaActual].second>7){
                    reinas[reinaActual].second = 0;
                }

                for(int y = 0;y<=7;y++){
                    conflictos += numConflictos(y);
                }

               //cout<<reinas[reinaActual].first+1<<"-"<<reinas[reinaActual].second+1<<";"<<conflictos<<endl;

                if(conflictos <= numConfActual){
                    columna = reinas[reinaActual].second;
                    numConfActual = conflictos;
                    //cout<<"Columna menos conflictiva "<<columna<<endl;
                }
                conflictos = 0;

            };

            reinas[reinaActual].second = columna;
            //cout<<reinas[reinaActual].first<<"-"<<reinas[reinaActual].second<<";"<<columna<<endl;

            conflicts = 0;
            reinaPasada = reinaActual;
        
    }
    return 0;
}


main(){
    int vueltas = 10000;

    minConflicts(vueltas);

    for (const auto& pair : reinas) {
        cout << "First: " << pair.first +1<< ", Second: " << pair.second +1<< endl;
    }
    int conflictos = 0;
    for(int y = 0;y<=7;y++){
        conflictos += numConflictos(y);
    }
    cout<<conflictos/2;

    return 0;
}
