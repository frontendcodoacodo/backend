const header = document.querySelector(".header");

header.innerHTML = `
        <div class="logo">
        <a href="index.html"><img src="{{ url_for('static', filename='img/logo-turismo.png') }}" alt="logo-viajes"></a>
        </div>
        <input type="checkbox" id="menu-bar"></input>
        <label for="menu-bar"> <i class="fa-solid fa-bars"></i><h6>Menu</h6></label>
        <div class="navbar">
        <ul class="navbar-links"> 
           <li><a href="index.html">Inicio</a></li>                
           <li><a href="#">Donde Ir +</a>
               <ul class="submenu">
                    <li><a href="mendoza.html">Mendoza</a></li>
                    <li><a href="sanjuan.html">San Juan</a></li>
                    <li><a href="tucuman.html">Tucuman</a></li>
                    <li><a href="corrientes.html">Corrientes</a></li>
               </ul>
           </li> 
           <li><a href="sobre_nosotros.html">Sobre Nosotros</a></li> 
           <li><a href="contacto.html" class="nav-menu-link_active" >Contacto</a></li>   
        </ul>                     
        </div> 
        <div class="buttons">
        <i class="fa-brands fa-whatsapp"></i> 
        <i class="fa-brands fa-facebook"></i>
        </div>
`;
