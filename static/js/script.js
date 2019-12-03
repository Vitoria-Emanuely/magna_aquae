$(document).ready(function () {
    $("#owl-homepage").owlCarousel({

        autoPlay: false, //Set AutoPlay to 3 seconds
        items: 3,
        itemsDesktop: [1199, 3],
        itemsDesktopSmall: [979, 3],
        navigation: true,
        navigationText: ["voltar", "próximo"],
        autoHeight: false,
    });

    $('.ui.dropdown')
        .dropdown()
    ;

    $('.ui.checkbox')
        .checkbox()
    ;

    var $section = $('section').first();
    $section.find('.panzoom').panzoom({
        $zoomIn: $section.find(".zoom-in"),
        $zoomOut: $section.find(".zoom-out"),
        $zoomRange: $section.find(".zoom-range"),
        $reset: $section.find(".reset")
    });


    $('#range-1').range({
        min: 0,
        max: 100,
        start: 0,
    });

    //Bacia
    $("body").on("click", ".adicionarBacia", function () {
        $('.modalAdicionarBacia').modal('show');
    });

    $("body").on("click", ".editarBacia", function () {
        $('.modalEditarBacia').modal('show');
    });

    $("body").on("click", ".excluirBacia", function () {
        $('.modalExcluirBacia').modal('show');
    });

    //Rio
    $("body").on("click", ".adicionarRio", function () {
        $('.modalAdicionarRio').modal('show');
    });

    $("body").on("click", ".editarRio", function () {
        $('.modalEditarRio').modal('show');
    });

    $("body").on("click", ".editarRio", function () {
        $('.modalEditarRio').modal('show');
    });

    $("body").on("click", ".excluirRio", function () {
        $('.modalExcluirRio').modal('show');
    });

    //Ponto
    $("body").on("click", ".adicionarPonto", function () {
        $('.modalAdicionarPonto').modal('show');
    });

    $("body").on("click", ".editarPonto", function () {
        $('.modalEditarPonto').modal('show');
    });

    $("body").on("click", ".excluirPonto", function () {
        $('.modalExcluirPonto').modal('show');
    });

    //Coleta
    $("body").on("click", ".adicionarColeta", function () {
        $('.modalAdicionarColeta').modal('show');
    });

    $("body").on("click", ".infoColeta", function () {
        $('.modalInfoColeta').modal('show');
    });

    $("body").on("click", ".excluirColeta", function () {
        $('.modalExcluirColeta').modal('show');
    });

    //Caso
    $("body").on("click", ".adicionarCaso", function () {
        $('.modalAdicionarCaso').modal('show');
    });

    $("body").on("click", ".editarCaso", function () {
        $('.modalEditarCaso').modal('show');
    });

    $("body").on("click", ".excluirCaso", function () {
        $('.modalExcluirCaso').modal('show');
    });

    //Entorno
    $("body").on("click", ".adicionarEntorno", function () {
        $('.modalAdicionarEntorno').modal('show');
    });

    $("body").on("click", ".excluirEntorno", function () {
        $('.modalExcluirEntorno').modal('show');
    });

    $("body").on("click", ".editarEntorno", function () {
        $('.modalEditarEntorno').modal('show');
    });

    //Cadastro
    $("body").on("click", ".cadastro", function () {
        $('.modalCadastro').modal('show');
    });

    $("body").on("click", ".recuperarSenha", function () {
        $('.modalRecuperarSenha').modal('show');
    });

    //Imagem
    $("body").on("click", ".adicionarImagem", function () {
        $('.modalAdicionarImagem').modal('show');
    });

    $("body").on("click", ".editarImagem", function () {
        $('.modalEditarImagem').modal('show');
    });

    $("body").on("click", ".excluirImagem", function () {
        $('.modalExcluirImagem').modal('show');
    });

    //Conta
    $("body").on("click", ".acessarConta", function () {
        $('.modalAcessarConta').modal('show');
    });

    //Monitoramento
    $("body").on("click", ".editarSolucao", function () {
        $('.modalEditarSolucao').modal('show');
    });

    $("body").on("click", ".utilizarSolucao", function () {
        $('.modalUtilizarSolucao').modal('show');
    });

    //Imagem
    $("body").on("click", ".excluirImagem", function () {
        $('.modalExcluirImagem').modal('show');
    });

    //Sobre
    $("body").on("click", ".sobre", function () {
        $('.modalSobre').modal('show');
    });

    //Usuário
    $("body").on("click", ".editarUsuario", function () {
        $('.modalEditarUsuario').modal('show');
    });

    $("body").on("click", ".editarSenha", function () {
        $('.modalEditarSenha').modal('show');
    });

    //Detalhes (Histórico)
    $(".modalImagem").click(function () {
        $(".modalDetalhes" + $(this).attr('id')).modal('show');
    });

    $("body").on("click", ".excluirMonitoramento", function () {
        $('.modalExcluirMonitoramento').modal('show');
    });

    //Publico
    $("body").on("click", ".visualizacao", function () {
        $('.modalPublico').modal('show');
    });

    //Copiar
    $("body").on("click", ".copiar", function () {
        $('.modalCopiar').modal('show');
    });
});
