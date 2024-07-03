const footer = document.querySelector(".footer");

footer.innerHTML = `

<div class="footer-nav">
    <div class="row">
        <div class="col">
            <img src="{{ url_for('static', filename='img/logo-turismo.png') }}" alt="" class="logo">
            <p>Vení a conocer cuatro de las provincias mas hermosas de nuestro país</p>
            
        </div>
        <div class="col">
            <h3>Datos de Contacto <div class="underline"><span></span></div> </h3>
            <p>República de Eslovenia 1901, C1426  </p>
            <p><br> Ciudad Autónoma de Buenos Aires </p>
            <p class="email-id">experienciaargentinaviajes@gmail.com</p>
            <h4>+54 011 101010</h4>
        </div>
        <div class="col">
            <h3>Links <div class="underline"><span></span></div> </h3>
            <ul>
                <li><a href="inicio.html">Inicio</a></li>
                <li><a href="sobre_nosotros.html">Sobre Nosotros</a></li>
                <li><a href="contacto.html">Contacto</a></li>
            </ul> 
            <div class="redes-sociales">
                <i class="fab fa-facebook-f"></i>
                <i class="fab fa-instagram"></i>
                <i class="fab fa-whatsapp"></i>
            </div>  
        </div>
    </div>  
    <hr>
    <p class="copyright">Experiencia Argentina Viajes @ 2024 - Todos los derechos reservados </p>
</div>

`;
