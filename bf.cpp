#include<iostream>
#include<stdint.h>
#include<stdio.h>
#include<stdlib.h>

using namespace std;

void gt(char* &data)
{
	data++;
}
void lt(char* &data)
{
	data--;
}
void ps(char* &data)
{
	(*data)++;
}
void ms(char* &data)
{
	(*data)--;
}
void dot(char* &data)
{
	printf("%c", *data);
}
void comma(char* &data)
{
	cin>>*data;
}
void lb(char* &data, char* &code)
{
	int rem=1;
	if(*data==0)
	{	while(rem!=0)
		{
			code++;
			if(*code=='[') rem++;
			else if(*code==']') rem--;
		}
	}	
}
void rb(char* &data, char* &code)
{
	int rem=1;
	if(*data!=0)
	{
		while(rem!=0)
		{
			code--;
			if(*code=='[') rem--;
			else if(*code==']') rem++;
		}
		code--;
	}
}
void pa(char* &code, char* &start)
{
	cout<<"Offset is "<<(code-start)<<endl;
}

int main(int argc, char **argv)
{
	char data[30000];
	char *d;
	d=data;
	FILE *f;
	f=fopen(argv[1], "r");
	fseek(f, 0, SEEK_END);
	int size=ftell(f);
	fseek(f, 0, SEEK_SET);
	char *code=(char *)malloc(size);
	fread(code, 1, size, f);
	while(*code)
	{
		switch(*code)
		{	
			case '+':
			{
				ps(d);
				break;
			}
			case '-':
			{	
				ms(d);
				break;
			}
			case '>':
			{
				gt(d);
				break;
			}
			case '<':
			{
				lt(d);
				break;
			}
			case '.':
			{
				dot(d);
				break;
			}
			case ',':
			{
				comma(d);
				break;
			}
			case '[':
			{
				lb(d, code);
				break;
			}
			case ']':
			{
				rb(d, code);
				break;
			}
		}
		code++;
	}
	return 0;
}
