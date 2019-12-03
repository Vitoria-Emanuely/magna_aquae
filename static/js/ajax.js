//
//Pesquisas e Modals
//

function bacia_para_rio() {
    if ($("select#bh").val() === 'selecione') {
        var options = '<option>Selecione primeiro uma bacia hidrográfica</option>';
        $("select#rio").html(options);
        $("select#rio").attr('disabled', true);
        var options = '<option>Selecione primeiro um rio</option>';
        $("select#ponto_monitoramento").html(options);
        $("select#ponto_monitoramento").attr('disabled', true);
        var options = '<option>Selecione primeiro um ponto</option>';
        $("select#coleta").html(options);
        $("select#coleta").attr('disabled', true);
    } else {
        $.ajax({
            type: 'GET',
            url: '/ajax/pesquisa/',
            data: {
                bh: $("select#bh").val(),
                csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
            },
            dataType: 'json',
            success: function (data) {
                var options = '<option>Selecione um rio</option>';
                for (var i = 0; i < data.length; i++) {
                    options += '<option value="' + data[i].pk + '">' + data[i].fields['nome'] + '</option>';
                }
                $("select#rio").html(options);
                $("select#rio").attr('disabled', false);
            },
            error: function (xhr, errmsg) {
                console.log(xhr.status + ": " + xhr.responseText + "Error: " + errmsg);
            }
        });
    }
    //Modal Rio
    if ($("select#bhModal").val() === 'selecione') {
        var options = '<option>Selecione primeiro uma bacia hidrográfica</option>';
        $("select#rioModal").html(options);
        $("select#rioModal").attr('disabled', true);
    } else {
        $.ajax({
            type: 'GET',
            url: '/ajax/pesquisa/',
            data: {
                bh: $("select#bhModal").val(),
                csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
            },
            dataType: 'json',
            success: function (data) {
                var options = '<option>Selecione um rio</option>';
                for (var i = 0; i < data.length; i++) {
                    options += '<option value="' + data[i].pk + '">' + data[i].fields['nome'] + '</option>';
                }
                $("select#rioModal").html(options);
                $("select#rioModal").attr('disabled', false);
            },
            error: function (xhr, errmsg) {
                console.log(xhr.status + ": " + xhr.responseText + "Error: " + errmsg);
            }
        });
    }
    //Modal Coleta
    if ($("select#bhModalColeta").val() === 'selecione') {
        var options = '<option>Selecione primeiro uma bacia hidrográfica</option>';
        $("select#rioModalColeta").html(options);
        $("select#rioModalColeta").attr('disabled', true);
    } else {
        $.ajax({
            type: 'GET',
            url: '/ajax/pesquisa/',
            data: {
                bh: $("select#bhModalColeta").val(),
                csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
            },
            dataType: 'json',
            success: function (data) {
                var options = '<option>Selecione um rio</option>';
                for (var i = 0; i < data.length; i++) {
                    options += '<option value="' + data[i].pk + '">' + data[i].fields['nome'] + '</option>';
                }
                $("select#rioModalColeta").html(options);
                $("select#rioModalColeta").attr('disabled', false);
            },
            error: function (xhr, errmsg) {
                console.log(xhr.status + ": " + xhr.responseText + "Error: " + errmsg);
            }
        });
    }
    //Modal Ponto
    if ($("select#bhModalPonto").val() === 'selecione') {
        var options = '<option>Selecione primeiro uma bacia hidrográfica</option>';
        $("select#rioModalPonto").html(options);
        $("select#rioModalPonto").attr('disabled', true);
    } else {
        $.ajax({
            type: 'GET',
            url: '/ajax/pesquisa/',
            data: {
                bh: $("select#bhModalPonto").val(),
                csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
            },
            dataType: 'json',
            success: function (data) {
                var options = '<option>Selecione um rio</option>';
                for (var i = 0; i < data.length; i++) {
                    options += '<option value="' + data[i].pk + '">' + data[i].fields['nome'] + '</option>';
                }
                $("select#rioModalPonto").html(options);
                $("select#rioModalPonto").attr('disabled', false);
            },
            error: function (xhr, errmsg) {
                console.log(xhr.status + ": " + xhr.responseText + "Error: " + errmsg);
            }
        });
    }
}

function rio_para_ponto() {
    if ($("select#rio").val() === 'selecione') {
        var options = '<option>Selecione primeiro um rio</option>';
        $("select#ponto_monitoramento").html(options);
        $("select#ponto_monitoramento").attr('disabled', true);
    } else {
        $.ajax({
            type: 'GET',
            url: '/ajax/pesquisa/',
            data: {
                rio: $("select#rio").val(),
                csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
            },
            dataType: 'json',
            success: function (data) {
                var options = '<option>Selecione um ponto</option>';
                for (var i = 0; i < data.length; i++) {
                    latlong = 'Latitude: ' + data[i].fields['latitude'] + ' -  Longitude:  ' + data[i].fields['longitude'];
                    options += '<option value="' + data[i].pk + '">' + latlong + '</option>';
                }
                $("select#ponto_monitoramento").html(options);
                $("select#ponto_monitoramento").attr('disabled', false);
            },
            error: function (xhr, errmsg) {
                console.log(xhr.status + ": " + xhr.responseText + "Error: " + errmsg);
            }
        });
    }
    //Modal Coleta
    if ($("select#rioModalColeta").val() === 'selecione') {
        var options = '<option>Selecione primeiro um rio</option>';
        $("select#ponto_monitoramentoModal").html(options);
        $("select#ponto_monitoramentoModal").attr('disabled', true);
    } else {
        $.ajax({
            type: 'GET',
            url: '/ajax/pesquisa/',
            data: {
                rio: $("select#rioModalColeta").val(),
                csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
            },
            dataType: 'json',
            success: function (data) {
                var options = '<option>Selecione um ponto</option>';
                for (var i = 0; i < data.length; i++) {
                    latlong = 'Latitude: ' + data[i].fields['latitude'] + ' -  Longitude:  ' + data[i].fields['longitude'];
                    options += '<option value="' + data[i].pk + '">' + latlong + '</option>';
                }
                $("select#ponto_monitoramentoModal").html(options);
                $("select#ponto_monitoramentoModal").attr('disabled', false);
            },
            error: function (xhr, errmsg) {
                console.log(xhr.status + ": " + xhr.responseText + "Error: " + errmsg);
            }
        });
    }
    //Ponto
    if ($("select#rioModalPonto").val() === 'selecione') {
        var options = '<option>Selecione primeiro um rio</option>';
        $("select#ponto_monitoramentoColeta").html(options);
        $("select#ponto_monitoramentoColeta").attr('disabled', true);
    } else {
        $.ajax({
            type: 'GET',
            url: '/ajax/pesquisa/',
            data: {
                rio: $("select#rioModalPonto").val(),
                csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
            },
            dataType: 'json',
            success: function (data) {
                var options = '<option>Selecione um ponto</option>';
                for (var i = 0; i < data.length; i++) {
                    latlong = 'Latitude: ' + data[i].fields['latitude'] + ' -  Longitude:  ' + data[i].fields['longitude'];
                    options += '<option value="' + data[i].pk + '">' + latlong + '</option>';
                }
                $("select#ponto_monitoramentoColeta").html(options);
                $("select#ponto_monitoramentoColeta").attr('disabled', false);
            },
            error: function (xhr, errmsg) {
                console.log(xhr.status + ": " + xhr.responseText + "Error: " + errmsg);
            }
        });
    }
}

function ponto_para_coleta() {
    if ($("select#ponto_monitoramento").val() === 'selecione') {
        var options = '<option>Selecione primeiro um ponto</option>';
        $("select#coleta").html(options);
        $("select#coleta").attr('disabled', true);
    } else {

    console.log('HDOASGHDUOAGDUOQWGUOQEQUBFÇJKAFHQEQWNEJQWHE');
        $.ajax({
            type: 'GET',
            url: '/imagem/add/',
            data: {
                ponto: $("select#ponto_monitoramento").val(),
                csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
            },
            dataType: 'json',
            success: function (data) {
                console.log(data);
                var options = '<option value="selecione">Selecione uma coleta</option>';
                for (var i = 0; i < data.length; i++) {
                    var mydate = new Date(data[i].fields['data_coleta']);
                    if ((mydate.getMonth() + 1).toString().length === 1) {
                        var dataok = (mydate.getDate() + 1) + "/0" + (mydate.getMonth() + 1) + "/" + mydate.getFullYear();
                    } else {
                        var dataok = (mydate.getDate() + 1) + "/" + (mydate.getMonth() + 1) + "/" + mydate.getFullYear();
                    }
                    options += '<option value="' + data[i].pk + '">' + dataok + '</option>';
                }
                $("select#coleta").html(options);
                $("select#coleta").attr('disabled', false);
            },
            error: function (xhr, errmsg) {
                console.log(xhr.status + ": " + xhr.responseText + "Error: " + errmsg);
            }
        });
    }

//Coleta
    if ($("select#ponto_monitoramentoModal").val() === 'selecione') {
        var options = '<option>Selecione primeiro um ponto</option>';
        $("select#coletaImagem").html(options);
        $("select#coletaImagem").attr('disabled', true);
    } else {
        $.ajax({
            type: 'GET',
            url: '/imagem/add/',
            data: {
                ponto: $("select#ponto_monitoramentoModal").val(),
                csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
            },
            dataType: 'json',
            success: function (data) {
                console.log(data);
                var options = '<option value="selecione">Selecione uma coleta</option>';
                for (var i = 0; i < data.length; i++) {
                    var mydate = new Date(data[i].fields['data_coleta']);
                    if ((mydate.getMonth() + 1).toString().length === 1) {
                        var dataok = mydate.getDate() + "/0" + (mydate.getMonth() + 1) + "/" + mydate.getFullYear();
                    } else {
                        var dataok = mydate.getDate() + "/" + (mydate.getMonth() + 1) + "/" + mydate.getFullYear();
                    }
                    options += '<option value="' + data[i].pk + '">' + dataok + '</option>';
                }
                $("select#coletaImagem").html(options);
                $("select#coletaImagem").attr('disabled', false);
            },
            error: function (xhr, errmsg) {
                console.log(xhr.status + ": " + xhr.responseText + "Error: " + errmsg);
            }
        });
    }
}

//Não é para estar usando


//     if ($("select#ponto_monitoramentoColeta").val() === 'selecione') {
//         var options = '<option>Selecione primeiro um ponto</option>';
//         $("select#coletaIm").html(options);
//         $("select#coletaIm").attr('disabled', true);
//     } else {
//         $.ajax({
//             type: 'GET',
//             url: '/imagem/add/',
//             data: {
//                 ponto: $("select#ponto_monitoramentoColeta").val(),
//                 csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
//             },
//             dataType: 'json',
//             success: function (data) {
//                 console.log(data);
//                 var options = '<option value="selecione">Selecione uma coleta</option>';
//                 for (var i = 0; i < data.length; i++) {
//                     var mydate = new Date(data[i].fields['data_coleta']);
//                     if ((mydate.getMonth()+1).toString().length === 1){
//                         var dataok = mydate.getDate()+"/0"+(mydate.getMonth()+1)+"/"+mydate.getFullYear();
//                     }else{
//                         var dataok = mydate.getDate()+"/"+(mydate.getMonth()+1)+"/"+mydate.getFullYear();
//                     }
//                     options += '<option value="' + data[i].pk + '">' + dataok + '</option>';
//                 }
//                 $("select#coletaIm").html(options);
//                 $("select#coletaIm").attr('disabled', false);
//             },
//             error: function (xhr, errmsg) {
//                 console.log(xhr.status + ": " + xhr.responseText + "Error: " + errmsg);
//             }
//         });
//     }
// }

//Botão Pŕoximo Passo
function enviar() {
    $("button.botao").removeAttr('disabled');
}

//
//Bacia Hidrográfica
//

function bh_editar(id) {
    $.ajax({
        type: 'GET',
        url: '/bacia-hidrografica/edit/',
        data: {
            bacia: id,
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
        },
        dataType: 'json',
        success: function (data) {
            $("input#nome_bh").attr('value', data[0].fields['nome']);
            $("input#id_bh").attr('value', data[0].pk);
        },
        error: function (xhr, errmsg) {
            console.log(xhr.status + ": " + xhr.responseText + "Error: " + errmsg);
        }
    });
}

function bh_excluir(id) {
    var nome = $("input#" + id).val();
    $("span#nome").html(nome);
    var link = 'delete/' + id;
    $("a#link").attr('href', link);
}

//
// Rio
//

function rio_pesquisar_bacia() {
    if ($("input[name='bacia_hidro']").val() === 'selecione') {
        window.location.href = '/rio/';
    } else {
        $.ajax({
            type: 'POST',
            url: '/rio/',
            data: {
                bh: $("input[name='bacia_hidro']").val(),
                csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
            },
            dataType: 'json',
            success: function (data) {
                var rios = '';
                if (data.length === 0) {
                    rios += '<tr><td>Não há dados cadastrados.</td></tr>';
                } else {
                    var bacia = $('div').find("[data-value='" + $("input[name='bacia_hidro']").val() + "']").text();
                    for (var i = 0; i < data.length; i++) {
                        rios += '<tr>' +
                            '<td>' + data[i].fields['nome'] + '</td>' +
                            '<td>' + data[i].fields['dimensao'] + '</td>' +
                            '<td id="bacia' + data[i].pk + '">' + bacia + '</td>' +
                            '<td class="collapsing center aligned">' +
                            '<a class="cursorPointer editarRio" onclick="rio_editar(' + data[i].pk + ')">' +
                            '<i class="ui write grey large icon"></i>' +
                            '</a>' +
                            '</td>' +
                            '<td class="collapsing center aligned">' +
                            '<a class="cursorPointer excluirRio" onclick="rio_excluir(' + data[i].pk + ')">' +
                            '<i class="ui trash red large icon"></i>' +
                            '</a>' +
                            '</td>';
                        if (data[i].fields['publico'] === true) {
                            rios += '<td class="collapsing center aligned"><div class="ui fitted toggle checkbox visualizacao tooltip" data-tooltip="Público" ' +
                                'data-position="top center" onclick="publico(' + data[i].pk + ')"><i class="ui eye green large icon"></i></div></td>';
                        } else {
                            rios += '<td class="collapsing center aligned"><div class="ui fitted toggle checkbox visualizacao tooltip" data-tooltip="Privado" ' +
                                'data-position="top center" onclick="publico(' + data[i].pk + ')"><i class="ui eye slash outline large icon"></i></div></td>';
                        }
                        rios += '</tr>';
                    }

                }
                $("tbody#tbrio").html(rios);
            },
            error: function (xhr, errmsg) {
                console.log(xhr.status + ": " + xhr.responseText + "Error: " + errmsg);
            }
        });
    }

    if ($("input[name='bacia_hidro_outros']").val() === 'selecione') {
        window.location.href = '/rio/';
        var teste = '';
        teste += '<div class="ui tab tabular attached bottom segment active"  data-tab="second">';
        $("article#teste").html(teste);

    } else {
        $.ajax({
            type: 'POST',
            url: '/rio/',
            data: {
                bh: $("input[name='bacia_hidro_outros']").val(),
                csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
            },
            dataType: 'json',
            success: function (data) {
                var rios = '';
                if (data.length === 0) {
                    rios += '<tr><td>Não há dados cadastrados.</td></tr>';
                } else {
                    var bacia = $('div').find("[data-value='" + $("input[name='bacia_hidro_outros']").val() + "']").text();
                    for (var i = 0; i < data.length; i++) {
                        rios += '<tr>' +
                            '<td>' + data[i].fields['nome'] + '</td>' +
                            '<td>' + data[i].fields['dimensao'] + '</td>' +
                            '<td id="bacia' + data[i].pk + '">' + bacia + '</td>' +
                            '<td class="collapsing center aligned">' +
                            '<input type="hidden" id="' + data[i].pk + '" value="' + data[i].fields['nome'] + '"/>' +
                            '<a class="cursorPointer copiar" onclick="copiar(' + data[i].pk + ')">' +
                            '<i class="ui copy blue large icon"></i>' +
                            '</a>' +
                            '</td>' +
                            '</tr>';
                    }

                }
                $("tbody#tbrio_outros").html(rios);
            },
            error: function (xhr, errmsg) {
                console.log(xhr.status + ": " + xhr.responseText + "Error: " + errmsg);
            }
        });

    }
}

function rio_editar(id) {
    $.ajax({
        type: 'GET',
        url: '/rio/edit/',
        data: {
            rio_id: id,
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
        },
        dataType: 'json',
        success: function (data) {
            $("input#nome_rio").attr('value', data[0].fields['nome']);
            $("input#dimensao_rio").attr('value', data[0].fields['dimensao']);
            $("input#bh_rio").attr('value', $("td#bacia" + id).text());
            $("input#id_rio").attr('value', data[0].pk);

        },
        error: function (xhr, errmsg) {
            console.log(xhr.status + ": " + xhr.responseText + "Error: " + errmsg);
        }
    });
}

function rio_excluir(id) {
    var nome = $("input#" + id).val();
    $("span#nome").html(nome);
    var link = 'delete/' + id;
    $("a#link").attr('href', link);
}

//
// Ponto
//

function ponto_editar(id) {
    $.ajax({
        type: 'GET',
        url: '/ponto/edit/',
        data: {
            ponto_id: id,
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
        },
        dataType: 'json',
        success: function (data) {
            $("input#ponto_lat").attr('value', data[0].fields['latitude']);
            $("input#ponto_lon").attr('value', data[0].fields['longitude']);
            $("input#ponto_rio").attr('value', $("td#rio" + id).text());
            $("input#ponto_bacia").attr('value', $("td#bacia" + id).text());
            $("input#id_ponto").attr('value', data[0].pk);
        },
        error: function (xhr, errmsg) {
            console.log(xhr.status + ": " + xhr.responseText + "Error: " + errmsg);
        }
    });
}

function ponto_excluir(id) {
    var link = 'delete/' + id;
    $("a#link").attr('href', link);
}

//
// Coleta
//

function coleta_info(id) {
    $.ajax({
        type: 'GET',
        url: '/coleta/info/',
        data: {
            id: id,
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
        },
        dataType: 'json',
        success: function (data) {
            data = $.parseJSON(data);
            var tab_rio = $("input[name=" + id + "][id=tab_rio]").val();
            var tab_data = $("input[name=" + id + "][id=tab_data]").val();
            var tab_ponto_latitude = $("input[name=" + id + "][id=tab_ponto_latitude]").val();
            var tab_ponto_longitude = $("input[name=" + id + "][id=tab_ponto_longitude]").val();
            var coleta = '<tr> <td>' + tab_rio + '</td> <td>' + '(' + tab_ponto_latitude + ' ; ' + tab_ponto_longitude
                + ')' + ' </td> <td>' + tab_data + ' </td> </tr>';
            var sub = '';
            for (var i = 0; i < data.length; i++) {
                sub += '<tr> <td>' + data[i][0] + '</td> <td>' + data[i][1] + '</td> </tr>';
            }
            $("tbody#tbinfo").html(coleta);
            $("tbody#tbsubs").html(sub);

        },
        error: function (xhr, errmsg) {
            console.log(xhr.status + ": " + xhr.responseText + "Error: " + errmsg);
        }
    });
}

function coleta_excluir(id) {
    var nome = $("input#" + id).val();
    $("span#nome").html(nome);
    var link = 'delete/' + id;
    $("a#link").attr('href', link);
}

//
//Caso
//

function caso_excluir(id) {
    var link = 'delete/' + id;
    $("a#link").attr('href', link);
}

function caso_editar(id) {
    $.ajax({
        type: 'GET',
        url: '/caso/edit/',
        data: {
            caso_id: id,
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
        },
        dataType: 'json',
        success: function (data) {
            $("input#iap").attr('value', $("td#iap").text());
            $("input#iva").attr('value', $("td#iva").text());
            $("input#variavel_entorno").attr('value', $("td#variavel_entorno" + id).text());
            $("input#risco").attr('value', $("td#risco").text());
            $("textarea#solucao").val(data[0].fields['solucao_sugerida']);
            $("textarea#solucao").attr('value', data[0].fields['solucao_sugerida']);
            $("input#id_caso").attr('value', data[0].pk);
        },
        error: function (xhr, errmsg) {
            console.log(xhr.status + ": " + xhr.responseText + "Error: " + errmsg);
        }
    });
}

//
//Entorno
//

function entorno_excluir(id) {
    var link = 'delete/' + id;
    $("a#link").attr('href', link);
}

function entorno_editar(id) {
    $.ajax({
        type: 'GET',
        url: '/entorno/edit/',
        data: {
            entorno_id: id,
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
        },
        dataType: 'json',
        success: function (data) {
            $("input#variavel_entorno").attr('value', data[0].fields['variavel_entorno']);
            $("input#cor").attr('value', data[0].fields['cor']);
            $("input#id_entorno").attr('value', data[0].pk);
        },
        error: function (xhr, errmsg) {
            console.log(xhr.status + ": " + xhr.responseText + "Error: " + errmsg);
        }
    });
}

//
//Imagem
//

function img_excluir(id) {
    var link = 'delete/' + id;
    $("a#link").attr('href', link);
}

function img_editar(id) {
    $.ajax({
        type: 'GET',
        url: '/imagem/edit/',
        data: {
            imagem_id: id,
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
        },
        dataType: 'json',
        success: function (data) {
            $("input#titulo").attr('value', data[0].fields['titulo']);
            $("input#data_emissao").attr('value', data[0].fields['data_emissao']);
            $("input#imagem_id").attr('value', data[0].pk);
        },
        error: function (xhr, errmsg) {
            console.log(xhr.status + ": " + xhr.responseText + "Error: " + errmsg);
        }
    });
}


//
// Monitoramento
//

var id_cache = '';

function monitoramento_imagem(id, id_coleta) {
    $("input#imagem").attr('value', id);
    $("input#coleta").attr('value', id_coleta);
    $("span#corner" + id).html('<a class="ui left green corner label"><i class="checkmark icon"></i></a>');
    if (id_cache != '') {
        $("span#corner" + id_cache).html('');
    }
    id_cache = id;
}

function monitoramento_entorno(id) {
    $("input#entorno").attr('value', id);
}

function monitoramento_solucao(id) {
    $("input#caso").attr('value', id);

}

function mon_excluir(id) {
    var link = '/historico/detalhes/delete/' + id;
    $("a#link").attr('href', link);
}

function monitoramento_editar(id) {
    $.ajax({
        type: 'GET',
        url: '/ajax/pesquisa/',
        data: {
            caso: id,
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
        },
        dataType: 'json',
        success: function (data) {
            var options = '';
            var risco = data[0].fields['risco'];
            var solucao = data[0].fields['solucao_sugerida'];
            if (risco === 'A') {
                options = '<option value="B">Baixo</option><option value="M">Médio</option><option selected value="A">Alto</option>';
            } else if (risco === 'M') {
                options = '<option value="B">Baixo</option><option selected value="M">Médio</option><option value="A">Alto</option>';
            } else {
                options = '<option selected value="B">Baixo</option><option value="M">Médio</option><option value="A">Alto</option>';
            }
            $("input#caso").attr('value', id);
            $("select#id_risco").html(options);
            $("textarea#id_solucao_sugerida").html(solucao);
        },
        error: function (xhr, errmsg) {
            console.log(xhr.status + ": " + xhr.responseText + "Error: " + errmsg);
        }
    });

}

function abrir() {
    $('.modalAdcSol').modal('show');
}

//
// Publico (visualização)
//

function publico(id, bacia, page) {
    var nome = $("input#" + id).val();
    $("span#nome").html(nome);
    var link = 'publico/' + id + '/' + bacia + '/' + page;
    $("a#publico").attr('href', link);
}

//
// Page (edit)
//

function page(bacia, page) {
    $("input#bacia").attr('value', bacia);
    $("input#page").attr('value', page);
}

//
// Abas
//

$('.top.menu .item').tab();

//
// Copiar
//

function copiar(id) {
    var nome = $("input#" + id).val();
    $("span#nome").html(nome);
    var link = 'copy/' + id;
    $("a#copiar").attr('href', link);
}

//
// Histórico
//

function checarSenha() {
    $("button#alterar").attr('disabled', false);
}

function senhaAntiga() {
    var senha1 = $("input[name='senha']").val();
    var senha2 = $("input[name='senha2']").val();

    $("input#senha").attr('value', senha1);
    $("input#senha2").attr('value', senha2);
}

//
//Recuperar Senha
//
var form_being_submitted = false;

function checkForm(form){
if(form.email.value === ""){
  form.email.focus();
  return false;
}
return true;
}
