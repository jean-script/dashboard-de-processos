



function dadosprocessos(id, status, processo_transaction_item,processo_transaction_number,processo_tempo_execucao, logs) {

    id_ = document.getElementById('processo_id').textContent=id;
    status_ = document.getElementById('processo_status').textContent=status;
    processo_transaction_item = document.getElementById('processo_transaction_item').textContent=processo_transaction_item;
    processo_transaction_number = document.getElementById('processo_transaction_number').textContent=processo_transaction_number;
    processo_tempo_execucao = document.getElementById('processo_tempo_execucao').textContent=processo_tempo_execucao;
    
    console.log(logs);
    
}