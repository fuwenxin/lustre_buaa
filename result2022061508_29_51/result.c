#include <stdlib.h>
#include <stdio.h>
#include <unistd.h>
#define bool char
#define ture 1
#define false 0
static int ISATTY;

void _put_bool(bool _V, char *s){
    if(ISATTY) {
        printf("%s: ", s);
        printf(_V?"true\n":"false\n");
    }
}
void _put_int(int _V, char *s){
    if(ISATTY) {
        printf("%s: %d\n", s, _V);
    }
}
void _put_real(float _V, char *s){
    if(ISATTY) {
        printf("%s: %f\n", s, _V);
    }
}

bool _get_bool(){
    int _V;
    if(ISATTY) scanf("%d", &_V);
    return (bool)_V;
}
int _get_int(){
    int _V;
    if(ISATTY) scanf("%d", &_V);
    return _V;
}
float _get_real(){
    float _V;
    if(ISATTY) scanf("%f", &_V);
    return _V;
}
int main(){
	int _s = 0;
	bool in_judge;
	int out_C;
	ISATTY = isatty(0);
	while(1) {
	if (ISATTY) printf("#step %d \n", _s++);
	in_judge = _get_bool();
	if(in_judge){
	out_C = 20;
	} else {
	out_C = 30;
	}
	_put_int(out_C, "out_C");
	}
	return 1;
}
