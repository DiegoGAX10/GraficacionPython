//Ejemplo de prueba para una escena vista 3D
//Por: Mario H Tiburcio Z

#include "colors.inc"
#include "librerias.inc"

camera {
  location <6,6,-6>
  look_at <0,0,0>
}

light_source {<4,5,-6> color White}
#declare pa=<5,0,0>;
#declare pb=<0,3,0>;
#declare pc=<0,0,0>;
#declare pd=<5,0,2>;
#declare pe=<0,3,2>;
#declare pf=<0,0,2>;
#declare calza=union{
object{
triangle{pa,pb,pc}
pigment{color Red}
}
object{
triangle{pa,pb,pc}
pigment{color Red}}

object{
triangle{pd,pe,pf}
pigment{color Blue}
}

object{
triangle{pc,pb,pe}
pigment{color Green}
}

object{
triangle{pe,pf,pc}
pigment{color Green}
}

object{
triangle{pa,pd,pf}
pigment{color Green}
}

object{
triangle{pa,pc,pf}
pigment{color Green}
}

object{
triangle{pa,pd,pe}
pigment{color White}
}

object{
triangle{pa,pb,pe}
pigment{color White}
}
}//calza

object{
calza
/*scale<1,1,0.2> //
scale<-1,1,1> //refleja en yz
scale<1,1,-1> //
scale<1,-1,1> //refleja hacia abajo
translate<0,2,0>// lo traslada dos unidades para arriba
translate<0,-1,0> //se entierra en el piso
*/
rotate<0,30,0> //rota 30
/*matrix<
-1,0,0,
0,1,0,
0,0,1,
0,0,0
>
*/
}


plane  { y,0 pigment {checker Black White }}
ejes3D