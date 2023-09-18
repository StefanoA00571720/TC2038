#include <bits/stdc++.h>
using namespace std;

//Numero de nodos
#define V 11

//Se immprime la solución
//Vector de colores
void printSolution(int color[])
{
    static int solutionCount = 1;
    cout << "Solution " << solutionCount << ":" << endl;
    for (int i = 0; i < V; i++)
        cout << "Node " << i << " -> Color " << color[i] << endl;
    cout << endl;
    solutionCount++;
}

//Comprueba que el color asignado no este asignado a un vecino
//#grafo a checar, grafo, vector color, color asignado
bool isSafe(int v, bool graph[V][V], int color[], int c)
{
    for (int i = 0; i < V; i++)
        if (graph[v][i] && c == color[i])
            return false;
    return true;
}

//Funcion recursiva
//Grafica, numero de colores, vector con los colores asiganados, numero de vectores
bool graphColoringUtil(bool graph[V][V], int m, int color[], int v){
    //Caso base, cuando se llega se manda a imprimir los colores asigandos
    if (v == V)
    {
        printSolution(color);
        return true;
    }

    bool res = false;

    //For para probar todos los posibles colores
    for (int c = 1; c <= m; c++){
        //Se comprueba que el color asignado no sea el mismo que el de un vecino
        if (isSafe(v, graph, color, c)){
            color[v] = c;
            res = graphColoringUtil(graph, m, color, v + 1) || res;
            color[v] = 0; // Backtrack
        }
    }
    return res;
}

//Funcion para inicializar, grafica, numero de colores
void graphColoring(bool graph[V][V], int m){
    //Llenar el vector de color con 0s
    int color[V];
    for (int i = 0; i < V; i++)
    {
        color[i] = 0;
    }

    //Llamar a la función recursiva y ver si hay solución
    if (!graphColoringUtil(graph, m, color, 0))
    {
        cout << "No existe solución" << endl;
    }
}

int main(){

    //Grafo representando el mapa
    bool graph[V][V] = {
        {0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0},
        {1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0},
        {0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0},
        {1, 1, 0, 0, 1, 0, 1, 1, 0, 0, 0},
        {0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 0},
        {0, 1, 1, 0, 1, 0, 0, 0, 1, 0, 0},
        {0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0},
        {0, 0, 0, 1, 1, 0, 1, 0, 1, 1, 1},
        {0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 1},
        {0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1},
        {0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0}};

    //Numero de colores
    int m = 4;

    graphColoring(graph, m);

    return 0;
}
