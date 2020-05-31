void exponential(char *str, int len,float parameter);
void genrand(int len,char *str);
unsigned int  genran1( unsigned int start,unsigned int end);
double genran2(unsigned int start,unsigned int end,unsigned int len);
void uniform(char *str, int len);
void pareto(char *str,int len,float parameter);
void gaussian(char *str, int len,double mean);
void halfgaussian(char*str,int len,double mean);
void lognormal(char *str, int len,double loc_par);
void rayleigh(char*str,int len,double parameter);
void chisquarecen(char *str,int len);

void uniform(char *str, int len)
{
int i;
FILE *fp;

fp = fopen(str,"w");
//Generate numbers
for (i = 0; i < len; i++)
{
fprintf(fp,"%lf\n",(double)rand()/RAND_MAX);
}
fclose(fp);

}



unsigned int genran1( unsigned int start,unsigned int end)
{
	static unsigned rand=0xACE1U;
	if(start==end)
	return start;
	rand+=0x3AD;
	rand%=end;
	while(rand<start)
	{
		rand=rand+end -start;
	}
	return rand;
	//double t;
	//t=rand/end;
	//printf("%f\n",t);
}

double genran2(unsigned int start,unsigned int end, unsigned int len)
{
	double j;
	j=genran1(start,len);
	double s;
	s=j/len;
	return s;
}	

void genrand(int len,char *str)
{
	FILE*fp;
	fp=fopen(str,"w");	
	int i;
	for(i=0;i<len;i++)
	{
		fprintf(fp,"%f\n",genran2(0,i,len));
	}
	fclose(fp);
}	
		
			
	
	
			
void exponential(char *str, int len,float parameter)
{




//Generate numbers
if (parameter>0)
{
	int i;
	FILE *fp;
	fp = fopen(str,"w");
	for (i = 0; i < len; i++)
	{
		
		double z=log(1-genran2(0,i,len));
		z=z/(-parameter);
		fprintf(fp,"%lf\n",z);
	}
	fclose(fp);


}
else
{
	printf("Invalid value of parameter entered\n");
	printf("The parameter has to be greater than 0\n");
}	
	
}

void pareto(char *str,int len,float parameter)
{
	double z;
	if(parameter>=0)
	{
		int i;
	    FILE *fp;
	    fp = fopen(str,"w");
	    for(i=0;i<len;i++)
	    {
			z=pow((1-genran2(0,i,len)),(-parameter));
			z=(z-1)/parameter;
			fprintf(fp,"%lf\n",z);
		}
		fclose(fp);
	}
	else
	{
		int i;
	    FILE *fp;
	    fp = fopen(str,"w");
	    for(i=0;i<len;i++)
	    {
			z=pow(1+genran2(0,i,len)/parameter,(-parameter));
			z=(z-1)/parameter;
			fprintf(fp,"%lf\n",z);
		}
		fclose(fp);	
	}
}			

//Gaussian with  variance 1		
void gaussian(char*str,int len,double mean)
{
	int i;
	FILE*fp;
	fp=fopen(str,"w");
	for(i=0;i<len;i++)
	{
		double s;
		s=1-2*genran2(0,i,len);
		s=s*s;
		s=1-s;
		s=-log(s)*(M_PI/2);
		s=sqrt(s);
		s=abs(s+mean);
		fprintf(fp,"%f\n",s);
	}
	fclose(fp);
}	

void halfgaussian(char*str,int len,double mean)
{
	int i;
	FILE*fp;
	fp=fopen(str,"w");
	for(i=0;i<len;i++)
	{
		double s;
		s=1-2*genran2(0,i,len);
		s=s*s;
		s=1-s;
		s=-log(s)*(M_PI/2);
		s=sqrt(s);
		s=fabs(s+mean);
		fprintf(fp,"%f\n",s);
	}
	fclose(fp);
}
	
		
				
//Scale parameter and shape parameter are 0
void lognormal(char*str,int len,double loc_par)
{
	int i;
	FILE*fp;
	fp=fopen(str,"w");
	for(i=0;i<len;i++)
	{
		double s;
		s=1-2*genran2(0,i,len);
		s=s*s;
		s=1-s;
		s=-log(s)*(M_PI/2);
		s=sqrt(s);
		s=exp(s);
		s=s+loc_par;
		fprintf(fp,"%f\n",s);
	}
	fclose(fp);	
}	
				
		
void rayleigh(char *str,int len,double parameter)	
{
	double t=0;
	if(parameter>=t)
	{
		
		FILE *fp;
		fp = fopen(str,"w");
		int i;
		for(i=0;i<len;i++)
	    {
			double z=log(1-(double)rand()/RAND_MAX);
			z=-(z*parameter)*(2*parameter);
			z=sqrt(z);
			fprintf(fp,"%lf\n",z);
		}
		fclose(fp);
	}
	else
	printf("Invalid value of parameter entered\n");
}	

//Given degree of freedom is 2 therefore cdf of central chisquare distribution would be 1-e^(x/2)	

void chisquarecen(char *str,int len)
{
	FILE*fp;
	fp=fopen(str,"w");
	int i;
	for(i=0;i<len;i++)
	{
		double z=-log(1-(double)rand()/RAND_MAX);
		z=2*z;
		fprintf(fp,"%lf\n",z);
	}
	fclose(fp);
}		
				
//Rician distribution with (v,sigma) as parmeters then , sigma =1(given) then Rician(v,1) would be a noncentral chi distribution with two degrees of freedom and noncentrality parameter ν .
