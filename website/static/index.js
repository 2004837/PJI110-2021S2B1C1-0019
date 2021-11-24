function incluir(item) {
  
    var nome=document.getElementById(item).innerText;
    var node = document.createElement("LI");                 // Create a <li> node
    var textnode = document.createTextNode(nome);         // Create a text node
    node.appendChild(textnode);                              // Append the text to <li>
    document.getElementById("pedido").appendChild(node).setAttribute("id",item+'_pedido'); 
    document.getElementById(item).setAttribute("onclick",null);
    funcao="deleta(\""+item+"_pedido\")";
    document.getElementById(item+'_pedido').setAttribute("onclick",funcao);
  
  }
  
  
  function deleta(id){
  document.getElementById(id).remove();
  volta=id.substr(0,6);
  fvolta="incluir(\""+volta+"\")";
  document.getElementById(volta).setAttribute("onclick",fvolta);
  }
  
  function montarComanda(){
  document.getElementById("pedido").setAttribute("class","comanda col-4");
  document.getElementById("nome").setAttribute("class","x");
  document.getElementById("marmitex").setAttribute("class","x");
  }
  
  function imprimirComanda(){
  document.getElementById("pedido").setAttribute("style","background-color:#ffff99;");
  }
