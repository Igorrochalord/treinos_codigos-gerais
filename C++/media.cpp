#include <iostream>
#include <stdlib.h>
using namespace std;
int main(){

struct media
{
    char aluno[50];
    float nota;
    struct media*proximo;
};

struct media*nota1;
struct media*nota2;
while (true)
{
    nota1=(struct media)malloc(sizeof(struct media));
    cout<<"nome do aluno: ";
    cin>>nota1->aluno;
    cout<<"nota recebida: ";
    cin>>nota1->nota;
    cout<<"deseja ver sua media: [1] Sim [0] Nao ";
    int x;
    cin>>x;
    if (x==true)   //*true = 1
    {
        cout<<nota1->aluno<<endl;
        cout<<nota1->nota<<endl;
        
        break;
        
    }
    nota2=(struct media)malloc(sizeof(struct media));
    cout<<"nome do aluno: ";
    cin>>nota2->aluno;
    cout<<"nota recebida:  ";
    cin>>nota2->nota;
    cout<<"media: ";
    cout<<"deseja ver sua media : [1] Sim [0]Nao ";
    int y;
    cin>>y;
    if (y==true)
    {
        cout<<nota2->aluno<<endl;
        cout<<nota2->nota<<endl;
        break;
    }
    

}
return 0;}
