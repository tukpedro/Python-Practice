<h2 align="center">Sistema de Criptografia e Descriptografia de mensagens</h2>
<h4>Criptografia utilizada:</h4>
<ul>
	<li><a href="https://pt.wikipedia.org/wiki/Cifra_de_Vigen%C3%A8re">Cifra Vigenére</a></li>
</ul>
<h4>Descrição:</h4>
<p>A cifra de Vigenère consiste no uso de várias cifras de César em sequência, com diferentes valores de deslocamento ditados por uma "palavra-chave".</p>
<p>Para cifrar, é usada uma tabela de alfabetos (<i>tabula recta</i>) que consiste no alfabeto escrito 26 vezes em diferentes linhas, cada um deslocado ciclicamente do anterior por uma posição.</p>
<p>As 26 linhas correspondem às 26 possíveis cifras de César. Uma palavra é escolhida como "palavra-chave", e cada letra desta palavra vai indicar a linha a ser utilizada para cifrar ou decifrar uma letra da mensagem.</p>
<div align="center"><img src="https://crypto.interactive-maths.com/uploads/1/1/3/4/11345755/1889186_orig.jpg" alt="Tabula Recta" align="middle"></div>
<h4>Modo de uso:</h4>
<ul>
	
  <li>Digitar a mensagem à ser criptografada;</li>
  <li>Digitar a chave de criptografia;</li>
	<li>Será printada a mensagem <strong><u>criptografada</u></strong>;</li>
	<li>Digitar a chave para <strong><u>descriptografar</u></strong> a mensagem;</li>
  <li>Será printada a mensagem <strong><u>descriptografada.</u></strong></li>
</ul>
<h4>Foi utilizado:</h4>
<ul>
	<li>Python 3+;</li>
  <li>Jupyter;</li>
  <li>Módulo Getpass. Necessário instalar para ter a funcionalidade de ocultar caracteres de senha.</li>

</ul>
