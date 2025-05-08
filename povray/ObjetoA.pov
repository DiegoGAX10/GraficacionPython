#include "colors.inc"
#include "librerias.inc"

camera {
  location <14,14,-14>
  look_at <0,0,0>
}

light_source {<4,5,-6> color White}

#declare pa=<0,2,-7>;
#declare pb=<0,11,-7>;
#declare pc=<0,11,-3>;
#declare pd=<0,2,-3>;
#declare pe=<-8,2,-7>;
#declare pf=<-8,2,-3>;

#declare ObjetoA =union{      
triangle {pa,pb,pe pigment {color Yellow}}
triangle {pc,pd,pf pigment {color Yellow}}
// parte adef
triangle {pa,pd,pe pigment {color Blue}}
triangle {pe,pf,pd pigment {color Blue}} 
// parte abcd
triangle {pa,pb,pd pigment {color Green}}
triangle {pb,pc,pd pigment {color Green}}  
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
0,0,-0.5,
0,0.3333,0,
0.5,0,0
5.5,0.3333,1
> 
}


plane  { y,0 pigment {checker Black White }}
ejes3D