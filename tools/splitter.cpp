#include <string>
#include <fstream>
#include <iostream>
#include <vector>

using namespace std;
typedef char *pchar;
typedef unsigned short word;
typedef unsigned char uchar;

char *findnexthdr(char *p,int size)
{
  char *ps=p;
  if(p[0]!=0x1f || p[1]!=(char)0x8b){
    cerr<<"Invalid gzip part."<<hex<<(p[0]&0x00FF)<<" "<<(p[1]&0x00FF)<<endl;
    exit(2);
  }
  if(p[2]!=8){
    cerr<<"Invalid CM."; exit(2);
  }
  char f=p[3];
  p+=10;
  if(f&4) p+=2+*(word*)p;
  if(f&8) while(*p++);
  if(f&16) while(*p++);
  if(f&2) p+=2;
  size-=p-ps;
  while(size>0){
    while(size>0 && *p!=0x1f) {++p; --size;}
    if(size>0){
      if(p[1]==(char)0x8b && p[2]==8) return p;
      ++p; --size;
    }
  }
  return p;
}

int main(int argc, char **argv)
{
  --argc;
  if(argc==0){
    cerr<<"Need more arguments!"<<endl
        <<"Format: "<<*argv<<" filename1.h3c [filename2.h3c] ..."<<endl
        <<"Output file names are like filename1.h3c.1, etc."<<endl;
    return 1;
  }
  for(++argv; argc; --argc,++argv){
    cout<<"Opening file...";
    ifstream fs(*argv,ios::in|ios::binary);
    cout<<endl<<"Seek to the end...";
    fs.seekg(0,ios::end);
    cout<<endl<<"Reading the size...";
    int size=fs.tellg();
    cout<<size<<endl<<"Seek to the beginning...";
    fs.seekg(0);
    cout<<endl<<"Allocation buffer of size "<<size<<"...";
    char *data=new char[size];
    cout<<endl<<"Reading the data...";
    fs.read(data,size);
    cout<<endl<<"Closing the file...";
    fs.close();
    cout<<endl<<"Done reading."<<endl;
    vector<pchar> ptrs;
    cout<<"Scanning for parts...";
    for(char *p=data; p<data+size; p=findnexthdr(p,data+size-p))
      ptrs.push_back(p);
    ptrs.push_back(p);
    char *buffer=new char[strlen(*argv)+40];
    for(int i=1; i<ptrs.size(); ++i){
      sprintf(buffer,"%s.%d",*argv,i);
      ofstream fs(buffer,ios::out|ios::binary);
      fs.write(ptrs[i-1],ptrs[i]-ptrs[i-1]);
    }
    delete[]buffer;
    delete[]data;
    cout<<endl;
  }
  return 0;
}
