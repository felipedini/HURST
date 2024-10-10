O cálculo do Exponente de Hurst (H) é uma técnica usada para medir a autocorrelacion em uma série temporal, indicando a presença de dependências de longo prazo. O valor de H varia entre 0 e 1 e é interpretado da seguinte forma:

Quando H > 0.50
Quando o Exponente de Hurst é maior que 0.50, a série temporal é considerada persistente. Isso significa que a série exibe uma tendência a continuar na mesma direção. Em termos práticos:

Tendência de Continuidade: Se a série aumentou no passado, é provável que continue aumentando no futuro. Da mesma forma, se a série diminuiu no passado, é provável que continue diminuindo.
Longa Memória: A série tem uma memória de longo prazo, onde eventos passados têm uma influência duradoura sobre os futuros valores.
Exemplo: No mercado financeiro, um valor de H > 0.50 pode indicar uma tendência persistente de alta ou baixa nos preços dos ativos, sugerindo uma possível continuidade da tendência observada.
Quando H < 0.50
Quando o Exponente de Hurst é menor que 0.50, a série temporal é considerada anti-persistente. Isso significa que a série exibe uma tendência a reverter sua direção. Em termos práticos:

Tendência de Reversão: Se a série aumentou no passado, é provável que diminua no futuro. Da mesma forma, se a série diminuiu no passado, é provável que aumente.
Curta Memória: A série tem uma memória de curto prazo, onde eventos passados têm uma influência inversa sobre os futuros valores.
Exemplo: No mercado financeiro, um valor de H < 0.50 pode indicar uma tendência de reversão nos preços dos ativos, sugerindo que aumentos serão seguidos por quedas e vice-versa.

![image](https://github.com/user-attachments/assets/306261e6-c838-4661-9480-4394acf207ec)
