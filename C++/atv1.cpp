#include <iostream>
#include <stdlib.h>
using namespace std;
int main()
{
struct nota
{
    char aluno [50];
    float matricula;
    char curso[30];
    float nota1;
    float nota2;
    float nota3;
    float nota4;
    struct nota*proximo;
    struct nota*anterior;
};
    struct nota*p;
    struct nota*p1;
    struct nota*p2;
    
while (true)
{
p=(struct nota*)malloc(sizeof(struct nota));
struct nota*proximo;
cout<<"nome do aluno: ";
cin>>p->aluno;
cout<<"digite a matricula: ";
cin>>p->matricula;
cout<<"digite o curso matriculado: ";
cin>>p->curso;
cout<<"nota do 1ºB:";
cin>>p->nota1;
cout<<"nota do 2ºB:";
cin>>p->nota2;
cout<<"nota 3ºB:";
cin>>p->nota3;
cout<<"nota do AVD:";
cin>>p->nota4;
cout<<"deseja  mostrar [1]SIM ou deseja armazenar mais da dos  [0]armazenar: ";
int x;
cin>>x;
if (x == true)
{
    cout<<p->aluno<<endl;
    _sleep(2);
    cout<<p->matricula<<endl;
    _sleep(2);
    cout<<p->curso<<endl;
    _sleep(2);
    cout<<p->nota1<<endl;
    _sleep(2);
    cout<<p->nota2<<endl;
    _sleep(2);
    cout<<p->nota3<<endl;
    _sleep(2);
    cout<<p->nota4<<endl;
    _sleep(2);
    break;    
}
p1=(struct nota*)malloc(sizeof(struct nota));
struct nota*proximo;
cout<<"digite o aluno: ";
cin>>p1->aluno;
cout<<"digite a matricula: ";
cin>>p1->matricula;
cout<<"digite o curso: ";
cin>>p1->curso;
cout<<"nota do 1ºB:";
cin>>p1->nota1;
cout<<"nota do 2ºB:";
cin>>p1->nota2;
cout<<"nota do 3ºB";
cin>>p1->nota3;
cout<<"nota do avd";
cin>>p1->nota4;
cout<<"deseja  mostrar [1]SIM ou deseja armazenar mais da dos  [0]armazenar: ";
int y;
cin>>y;
if (y==1)
{
    cout<<p1->aluno<<endl;
    _sleep(2);
    cout<<p1->matricula<<endl;
    _sleep(2);
    cout<<p1->curso<<endl;
    _sleep(2);
    cout<<p1->nota1<<endl;
    _sleep(2);
    cout<<p1->nota2<<endl;
    _sleep(2);
    cout<<p1->nota3<<endl;
    _sleep(2);
    cout<<p1->nota4<<endl;
    _sleep(2);
    cout<<p->aluno<<endl;
    cout<<p->matricula<<endl;
    cout<<p->curso<<endl;
    cout<<p->nota1<<endl;
    cout<<p->nota2<<endl;
    cout<<p->nota3<<endl;
    cout<<p->nota4<<endl;
    break;
}
p2=(struct nota*)malloc(sizeof(struct nota));
struct nota*proximo;
cout<<"nome do aluno: ";
cin>>p2->aluno;
cout<<"digite a matricula: ";
cin>>p2->matricula;
cout<<"digite o curso matriculado: ";
cin>>p2->curso;
cout<<"nota do 1ºB:";
cin>>p2->nota1;
cout<<"nota do 2ºB:";
cin>>p2->nota2;
cout<<"nota 3ºB:";
cin>>p2->nota3;
cout<<"nota do AVD:";
cin>>p2->nota4;
cout<<"deseja  mostrar [1]SIM ou deseja armazenar mais da dos  [0]armazenar: ";
int t;
cin>>t;
if (t==true)
{
    cout<<p2->aluno<<endl;
    cout<<p2->curso<<endl;
    cout<<p2->matricula<<endl;
    cout<<p2->nota1<<endl;
    cout<<p2->nota2<<endl;
    cout<<p2->nota3<<endl;
    cout<<p2->nota4<<endl;
    break;
}
cout<<"ser vivos";
cout<<"----------";
cout<<"----------";
cout<<"----------";
cout<<"----------";
cout<<"ver um aluno em especifico ?[1]sim [2]nao";
int u;
cin>>u;
if (u==true)
{
cout<<p->aluno<<endl;
cout<<p1->aluno<<endl;
cout<<p2->aluno<<endl;
cout<<"qual deles deseja ver ? [aluno][aluno2][aluno3]";
return 0;
}
}
}