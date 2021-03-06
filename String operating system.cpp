#include <stdlib.h>
#include <iostream>
using namespace std;
#define MAX 1000
//字符串比较
int Str_cmp(char *s1, char *s2)
{
	while (*s1 == *s2)
	{
		if (*s1 == '\0')
			return 0;
		++s1;
		++s2;//相同且都比较完成输出0
	}
	if (*s1 > *s2)
		return 1;
	else
		return -1;//不同时结束循环，并比较
}
//字符串长度
int Str_len(char *str)
{
	int len = 0;
	while (*str != '\0')
	{
		len++;
		str++;
	}
	return len;
}
//字符串连接
char *Str_cat(char *s1, char *s2)
{
	while (*s1 != '\0')
		s1++;           //遍历s1，s1指向字符串1的\0
	while (*s2 != '\0')
	{
		*s1 = *s2;
		s1++;
		s2++;
	} //将s2的字符依次接在s1之后
	*s1 = '\0';          //在新字符串最后置入\0
	return s1;
}
//字符串查找
char *Str_str(char *str, char *key)
{
	char *p1, *p2, *head = str;
	if (*key == '\0')
		return(str);  //如果子字符串为空，返回字串1
	while (*head != '\0')
	{
		p1 = head;
		p2 = key;
		while (*p1 != '\0' && *p2 != '\0' && *p1 == *p2)
		{
			p1++;
			p2++;
		}    //从s1中找子字符串中的全部字符
		if (*p2 == '\0')
			return(head);      //查找成功，返回q指针
		head++;
	}
	return(NULL);           //查找失败，返回空值
}
//字符串分词
char *Str_tok(char *str, const char *delim)
{
	static char *src = NULL;      //记下上一次非分隔字符串字符的位置
	const char *indelim = delim;  //对delim做一个备份
	int flag = 1, index = 0;      //每一次调用strtok,flag标记都会使得程序只记录下第一个非分隔符的位置,以后出现非分隔符不再处理
	char *temp = NULL;            //程序的返回值
	if (str == NULL)
		str = src;                //若str为NULL则表示该程序继续处理上一次余下的字符串
	for (; *str; str++)
	{
		delim = indelim;
		for (; *delim; delim++)
		{
			if (*str == *delim)
			{
				*str = NULL;      //若找到delim中感兴趣的字符,将该字符置为NULL
				index = 1;        //用来标记已出现感兴趣字符
				break;
			}
		}
		if (*str != NULL&&flag == 1){
			temp = str;           //只记录下当前第一个非感兴趣字符的位置
			flag = 0;
		}
		if (*str != NULL&&flag == 0 && index == 1){
			src = str;                                   //第二次出现非感兴趣字符的位置(之前一定出现过感兴趣字符)
			return temp;
		}
	}
	src = str;                     //执行该句表明一直未出现过感兴趣字符,或者说在出现了感兴趣的字符后,就没再出现过非感兴趣字符
	return temp;
}
void In1(char s[])
{
	cout << "请输入字符串(回车结束):";
	getchar();
	gets(s);
}
void In2(char s1[], char s2[])
{
	cout << "请输入第一个字符串(回车结束):";
	getchar();
	gets(s1);

	cout << "请输入第二个字符串(回车结束):";
	gets(s2);
}
void menu()
{
	int n;
	char s1[MAX], s2[MAX];
	while (1)
	{
		cout << "【请输入想要实现的功能】：";
		cin >> n;
		switch (n)
		{
		case 1:
			cout << "[字符串比较]" << endl;
			In2(s1, s2);
			cout << "比较结果:" << Str_cmp(s1, s2);
			break;
		case 2:
			cout << "[字符串求长度]" << endl;
			In1(s1);
			cout << "字符串长度:" << Str_len(s1);
			break;
		case 3:
			cout << "[字符串连接]" << endl;
			In2(s1, s2);
			Str_cat(s1, s2);
			cout << "连接之后的字符串:" << s1;
			break;
		case 4:
			cout << "[字符串查找]" << endl;
			In2(s1, s2);
			cout << "查找结果:";
			if (Str_str(s1, s2))
				cout << Str_str(s1, s2);
			else
				cout << "NULL";
			break;
		case 5:
			char *temp;
			cout << "[字符串分词]" << endl;
			In2(s1, s2);
			temp = Str_tok(s1, s2);
			cout << "切割后的字符串:";
			while (temp)
			{
				cout << temp << endl;
				temp = Str_tok(NULL, s2);
			}
			break;
		default:
			cout << "退出字符串函数操作系统" << endl;
			return;
		}
		cout << endl << endl;
	}
}
int main()
{
	cout << "————————————ASCII字符串函数操作系统———————————" << endl;
	cout << "—————————————字符串比较请输入1—————————————" << endl;
	cout << "—————————————求字符串长度请输入2————————————" << endl;
	cout << "—————————————字符串连接请输入3—————————————" << endl;
	cout << "—————————————字符串查找请输入4—————————————" << endl;
	cout << "—————————————字符串分词请输入5—————————————" << endl;
	cout << "———————————————输入0结束———————————————" << endl;
	cout << "———————————————————————————————————" << endl;
	menu();
	system("pause");
	return 1;
}
