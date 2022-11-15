#include <iostream>
#include <cstdlib>
#include <cstring>
using  namespace std;
struct aluno
{
    nome char[50];
    matricula float;
    curso char[50];
    struct aluno*proximo;
    struct aluno*anterior;
    struct aluno*passo;
};



if(novo){
        novo->valor = num;
        // próximo do novo nó aponta para o início da lista
        novo->proximo = *lista;
        // o anterior é nulo pois é o primeiro nó
        novo->anterior =  NULL;
        // se a lista não estiver vazia, o anterior do primeiro nó aponta para o novo nó
        if(*lista)
            (*lista)->anterior = novo;
        // o novo nó passa a ser o início da lista (o primeiro nó da lista)
        *lista = novo;
    }
    else
        cout<<"Erro ao alocar memoria!\n";
        
proximo=(struct aluno*)malloc(sizeof(struct aluno ));
cout<<"digite o nome do aluno: ";
cin>>proximo->nome;
cout<<"digite a matricula: ";
cin>>p->matricula;
cout<<"digite o curso: ";

proximo=(struct aluno*)malloc(sizeof(struct aluno ));
cout<<"digite o nome do aluno: ";
cin>>proximo->nome;
cout<<"digite a matricula: ";
cin>>proximo->matricula;
cout<<"digite o curso";
cin>>proximo->matricula;

    if (proximo==)
    {
        /* code */
    }
    