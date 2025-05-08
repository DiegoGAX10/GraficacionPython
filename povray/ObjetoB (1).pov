#include "colors.inc"
#include "librerias.inc"

camera {
  location <14,14,-14>
  look_at <0,0,0>
}

light_source {<4,5,-6> color White}

#declare pa=<2,1,1>;
#declare pb=<2,4,1>;
#declare pc=<4,4,1>;
#declare pd=<4,1,1>;
#declare pe=<2,1,5>;
#declare pf=<4,1,5>;

#declare ObjetoA =union{      
triangle {pa,pb,pe pigment {color Green}}
triangle {pc,pd,pf pigment {color Green}}
// parte adef
triangle {pa,pd,pe pigment {color Blue}}
triangle {pe,pf,pd pigment {color Blue}} 
// parte abcd
triangle {pa,pb,pd pigment {color Yellow}}
triangle {pb,pc,pd pigment {color Yellow}}  
// parte bcef
triangle {pb,pc,pf pigment {color Red}}
triangle {pb,pe,pf pigment {color Red}}



}// ObjetoA
ObjetoA
object{
ObjetoA
}

object{
ObjetoA

matrix <
0,0,2,
0,3,0,
-2,0,0
2,-1,-11
> 
}


plane  { y,0 pigment {checker Black White }}
ejes3D