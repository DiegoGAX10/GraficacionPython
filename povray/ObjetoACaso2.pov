#include "colors.inc"
#include "librerias.inc"

camera {
  location <14,14,-14>
  look_at <0,0,0>
}

light_source {<4,5,-6> color White}

#declare pa = <-1, 7, -3>;
#declare pb = <-1, 7, 0>;
#declare pc = <-1, 3, 0>;
#declare pd = <-1, 3, -3>;
#declare pe = <-3, 3, 0>;
#declare pf = <-3, 3, -3>;


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
0, 0.5, 0,
0, 0, -0.5,
-2, 0, 0,
0, -1.5, 2.5
>

}


plane  { y,0 pigment {checker Black White }}
ejes3D