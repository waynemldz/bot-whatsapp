const axios = require('axios');
const { Client } = require('whatsapp-web.js');
const qrcode = require('qrcode-terminal');

const client = new Client();

client.on('qr', (qr) => {
    console.log('QR CODE GERADO!\n');

    qrcode.generate(qr, {
        small: true
    });
});

client.on('ready', () => {
    console.log('WhatsApp conectado!');
});

client.on('message', async (message) => {
    if(message.from.includes('@g.us')){
        return
    }

    console.log('Mensagem recebida: ', message.body);

    try{

        const response = await axios.post(
            'http://127.0.0.1:8000/message',
            {
                message: message.body
            }
        );

        await message.reply(
            response.data.response
        );
    } catch (error) {
        console.log('Erro: ', error.message);

        await message.reply(
            'Erro ao processar mensagem.'
        );
    }
});

client.initialize();