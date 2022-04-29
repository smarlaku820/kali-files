#include <stdio.h>
#include <crypt.h>

int main(void) {

char *hashed;
hashed=crypt("SaiPavanMarlakunta","$1$bluejay820");
puts(hashed);
return 0;

}
