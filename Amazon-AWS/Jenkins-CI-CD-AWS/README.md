# **Documentação: Implementação de CI/CD com Jenkins na AWS**

**1. Introdução**
Este documento descreve o processo de configuração de uma esteira de CI/CD utilizando Jenkins para automatização de build de um repositório hospedado no GitHub. A solução foi implementada em uma instância EC2 da AWS e inclui as principais dificuldades encontradas ao longo do processo, bem como suas respectivas soluções.

---

**2. Processo de desenvolvimento**

**2.1 Jenkins local e a limitação do webhook**
Inicialmente, o Jenkins foi instalado e configurado localmente. No entanto, foi identificado que para utilizar webhooks do GitHub e acionar jobs automaticamente a cada push, era necessário que o Jenkins estivesse acessível publicamente. Com isso, optou-se por hospedar o Jenkins em uma instância EC2 da AWS.

<img src="img\jenkins-pipeline.png">

**2.2 Escolha equivocada da região da instância**
A primeira instância EC2 criada foi alocada na região "Ohio". Contudo, houve dificuldades de conexão, principalmente devido a restrições de rede e latência. A solução foi criar uma nova instância na região de São Paulo, mais próxima geograficamente, o que melhorou a estabilidade de conexão.

**2.3 Problemas com o tipo de instância (t2.micro)**
Visando economia, a instância t2.micro (com 1 vCPU e 1 GB de RAM) foi inicialmente escolhida. No entanto, durante a execução das builds, observou-se lentidão excessiva e falhas por falta de recursos. A solução foi trocar para uma instância t3.small, que oferece 2 vCPUs e 2 GB de RAM, possibilitando a execução dos jobs de forma mais eficiente.

**2.4 Dependências ausentes: npm e pip**
Durante os primeiros testes de build, os scripts falhavam por falta do gerenciador de pacotes do Node.js (`npm`) e do Python (`pip`). Para corrigir isso, foi necessário instalar manualmente essas dependências na instância:

```bash
# Instalar Node.js e npm
curl -fsSL https://deb.nodesource.com/setup_18.x | sudo -E bash -
sudo apt-get install -y nodejs

# Instalar Python3 e pip
sudo apt install python3 python3-pip -y
```
---

**3. Instalação do Jenkins na EC2**

```bash
# Atualizar pacotes	sudo apt update && sudo apt upgrade -y

# Instalar Java (necessário para Jenkins)
sudo apt install openjdk-17-jre -y

# Adicionar o repositório do Jenkins
wget -O - https://pkg.jenkins.io/debian/jenkins.io-2023.key | sudo tee /usr/share/keyrings/jenkins-keyring.asc > /dev/null
echo "deb [signed-by=/usr/share/keyrings/jenkins-keyring.asc] https://pkg.jenkins.io/debian binary/" | sudo tee /etc/apt/sources.list.d/jenkins.list > /dev/null

# Atualizar e instalar Jenkins
sudo apt update
sudo apt install jenkins -y

# Iniciar e habilitar Jenkins
sudo systemctl start jenkins
sudo systemctl enable jenkins

# Liberar a porta 8080
sudo ufw allow 8080
sudo ufw enable
```

---

**4. Configuração do Webhook no GitHub**
Com o Jenkins acessível via IP público, foi possível configurar um webhook no GitHub para notificar o Jenkins a cada push. Foi utilizado o plugin "GitHub Integration" e configurado um pipeline declarativo para automatizar os processos de build.

<img src="img\jenkins-triger.png">
<img src="img\github-webhook.png">


---

**5. Considerações finais**

O processo de implantação do Jenkins em ambiente cloud apresentou vários desafios, como limitações de rede, escolha inadequada de região e tipo de instância, bem como dependências de ambiente não previamente instaladas. No entanto, todas as questões foram contornadas, e o sistema de CI/CD encontra-se funcional para testes e projetos de pequeno porte.

Para ambientes de produção ou com maior volume de builds, recomenda-se considerar instâncias mais robustas e aplicar boas práticas de segurança, como uso de HTTPS, autenticação com tokens e roles IAM.



