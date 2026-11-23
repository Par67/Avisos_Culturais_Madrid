# -*- coding: utf-8 -*-
"""
Gera os audios do «Presente do indicativo» (Departamento de Portugues - EOI de Mostoles).
Portugal: voz pt-PT-RaquelNeural   ·   Brasil: voz pt-BR-ThalitaNeural
No fim cria o ficheiro audios_presente.zip nesta mesma pasta.
"""
import asyncio, os, sys, zipfile

try:
    import edge_tts
except ImportError:
    print("Falta o edge-tts. Escreva primeiro:  pip install edge-tts")
    sys.exit(1)

VOZES = {"pt": "pt-PT-RaquelNeural", "br": "pt-BR-ThalitaNeural"}
VELOCIDADE = "-5%"
ITENS = {
"pt": [
[
"f_abrir_0",
"Eu abro."
],
[
"f_abrir_1",
"Tu abres."
],
[
"f_abrir_2",
"Ele abre."
],
[
"f_abrir_3",
"Nós abrimos."
],
[
"f_abrir_4",
"Eles abrem."
],
[
"f_acabar_0",
"Eu acabo."
],
[
"f_acabar_1",
"Tu acabas."
],
[
"f_acabar_2",
"Ele acaba."
],
[
"f_acabar_3",
"Nós acabamos."
],
[
"f_acabar_4",
"Eles acabam."
],
[
"f_acender_0",
"Eu acendo."
],
[
"f_acender_1",
"Tu acendes."
],
[
"f_acender_2",
"Ele acende."
],
[
"f_acender_3",
"Nós acendemos."
],
[
"f_acender_4",
"Eles acendem."
],
[
"f_achar_0",
"Eu acho."
],
[
"f_achar_1",
"Tu achas."
],
[
"f_achar_2",
"Ele acha."
],
[
"f_achar_3",
"Nós achamos."
],
[
"f_achar_4",
"Eles acham."
],
[
"f_acordar_0",
"Eu acordo."
],
[
"f_acordar_1",
"Tu acordas."
],
[
"f_acordar_2",
"Ele acorda."
],
[
"f_acordar_3",
"Nós acordamos."
],
[
"f_acordar_4",
"Eles acordam."
],
[
"f_acudir_0",
"Eu acudo."
],
[
"f_acudir_1",
"Tu acodes."
],
[
"f_acudir_2",
"Ele acode."
],
[
"f_acudir_3",
"Nós acudimos."
],
[
"f_acudir_4",
"Eles acodem."
],
[
"f_admitir_0",
"Eu admito."
],
[
"f_admitir_1",
"Tu admites."
],
[
"f_admitir_2",
"Ele admite."
],
[
"f_admitir_3",
"Nós admitimos."
],
[
"f_admitir_4",
"Eles admitem."
],
[
"f_agir_0",
"Eu ajo."
],
[
"f_agir_1",
"Tu ages."
],
[
"f_agir_2",
"Ele age."
],
[
"f_agir_3",
"Nós agimos."
],
[
"f_agir_4",
"Eles agem."
],
[
"f_agradecer_0",
"Eu agradeço."
],
[
"f_agradecer_1",
"Tu agradeces."
],
[
"f_agradecer_2",
"Ele agradece."
],
[
"f_agradecer_3",
"Nós agradecemos."
],
[
"f_agradecer_4",
"Eles agradecem."
],
[
"f_ajudar_0",
"Eu ajudo."
],
[
"f_ajudar_1",
"Tu ajudas."
],
[
"f_ajudar_2",
"Ele ajuda."
],
[
"f_ajudar_3",
"Nós ajudamos."
],
[
"f_ajudar_4",
"Eles ajudam."
],
[
"f_almocar_0",
"Eu almoço."
],
[
"f_almocar_1",
"Tu almoças."
],
[
"f_almocar_2",
"Ele almoça."
],
[
"f_almocar_3",
"Nós almoçamos."
],
[
"f_almocar_4",
"Eles almoçam."
],
[
"f_alugar_0",
"Eu alugo."
],
[
"f_alugar_1",
"Tu alugas."
],
[
"f_alugar_2",
"Ele aluga."
],
[
"f_alugar_3",
"Nós alugamos."
],
[
"f_alugar_4",
"Eles alugam."
],
[
"f_andar_0",
"Eu ando."
],
[
"f_andar_1",
"Tu andas."
],
[
"f_andar_2",
"Ele anda."
],
[
"f_andar_3",
"Nós andamos."
],
[
"f_andar_4",
"Eles andam."
],
[
"f_ansiar_0",
"Eu anseio."
],
[
"f_ansiar_1",
"Tu anseias."
],
[
"f_ansiar_2",
"Ele anseia."
],
[
"f_ansiar_3",
"Nós ansiamos."
],
[
"f_ansiar_4",
"Eles anseiam."
],
[
"f_aparecer_0",
"Eu apareço."
],
[
"f_aparecer_1",
"Tu apareces."
],
[
"f_aparecer_2",
"Ele aparece."
],
[
"f_aparecer_3",
"Nós aparecemos."
],
[
"f_aparecer_4",
"Eles aparecem."
],
[
"f_aprender_0",
"Eu aprendo."
],
[
"f_aprender_1",
"Tu aprendes."
],
[
"f_aprender_2",
"Ele aprende."
],
[
"f_aprender_3",
"Nós aprendemos."
],
[
"f_aprender_4",
"Eles aprendem."
],
[
"f_arrumar_0",
"Eu arrumo."
],
[
"f_arrumar_1",
"Tu arrumas."
],
[
"f_arrumar_2",
"Ele arruma."
],
[
"f_arrumar_3",
"Nós arrumamos."
],
[
"f_arrumar_4",
"Eles arrumam."
],
[
"f_assistir_0",
"Eu assisto."
],
[
"f_assistir_1",
"Tu assistes."
],
[
"f_assistir_2",
"Ele assiste."
],
[
"f_assistir_3",
"Nós assistimos."
],
[
"f_assistir_4",
"Eles assistem."
],
[
"f_atrair_0",
"Eu atraio."
],
[
"f_atrair_1",
"Tu atrais."
],
[
"f_atrair_2",
"Ele atrai."
],
[
"f_atrair_3",
"Nós atraímos."
],
[
"f_atrair_4",
"Eles atraem."
],
[
"f_atravessar_0",
"Eu atravesso."
],
[
"f_atravessar_1",
"Tu atravessas."
],
[
"f_atravessar_2",
"Ele atravessa."
],
[
"f_atravessar_3",
"Nós atravessamos."
],
[
"f_atravessar_4",
"Eles atravessam."
],
[
"f_atribuir_0",
"Eu atribuo."
],
[
"f_atribuir_1",
"Tu atribuis."
],
[
"f_atribuir_2",
"Ele atribui."
],
[
"f_atribuir_3",
"Nós atribuímos."
],
[
"f_atribuir_4",
"Eles atribuem."
],
[
"f_barbear_0",
"Eu barbeio."
],
[
"f_barbear_1",
"Tu barbeias."
],
[
"f_barbear_2",
"Ele barbeia."
],
[
"f_barbear_3",
"Nós barbeamos."
],
[
"f_barbear_4",
"Eles barbeiam."
],
[
"f_bater_0",
"Eu bato."
],
[
"f_bater_1",
"Tu bates."
],
[
"f_bater_2",
"Ele bate."
],
[
"f_bater_3",
"Nós batemos."
],
[
"f_bater_4",
"Eles batem."
],
[
"f_beber_0",
"Eu bebo."
],
[
"f_beber_1",
"Tu bebes."
],
[
"f_beber_2",
"Ele bebe."
],
[
"f_beber_3",
"Nós bebemos."
],
[
"f_beber_4",
"Eles bebem."
],
[
"f_caber_0",
"Eu caibo."
],
[
"f_caber_1",
"Tu cabes."
],
[
"f_caber_2",
"Ele cabe."
],
[
"f_caber_3",
"Nós cabemos."
],
[
"f_caber_4",
"Eles cabem."
],
[
"f_cair_0",
"Eu caio."
],
[
"f_cair_1",
"Tu cais."
],
[
"f_cair_2",
"Ele cai."
],
[
"f_cair_3",
"Nós caímos."
],
[
"f_cair_4",
"Eles caem."
],
[
"f_cantar_0",
"Eu canto."
],
[
"f_cantar_1",
"Tu cantas."
],
[
"f_cantar_2",
"Ele canta."
],
[
"f_cantar_3",
"Nós cantamos."
],
[
"f_cantar_4",
"Eles cantam."
],
[
"f_chatear_0",
"Eu chateio."
],
[
"f_chatear_1",
"Tu chateias."
],
[
"f_chatear_2",
"Ele chateia."
],
[
"f_chatear_3",
"Nós chateamos."
],
[
"f_chatear_4",
"Eles chateiam."
],
[
"f_chegar_0",
"Eu chego."
],
[
"f_chegar_1",
"Tu chegas."
],
[
"f_chegar_2",
"Ele chega."
],
[
"f_chegar_3",
"Nós chegamos."
],
[
"f_chegar_4",
"Eles chegam."
],
[
"f_cobrir_0",
"Eu cubro."
],
[
"f_cobrir_1",
"Tu cobres."
],
[
"f_cobrir_2",
"Ele cobre."
],
[
"f_cobrir_3",
"Nós cobrimos."
],
[
"f_cobrir_4",
"Eles cobrem."
],
[
"f_comecar_0",
"Eu começo."
],
[
"f_comecar_1",
"Tu começas."
],
[
"f_comecar_2",
"Ele começa."
],
[
"f_comecar_3",
"Nós começamos."
],
[
"f_comecar_4",
"Eles começam."
],
[
"f_comer_0",
"Eu como."
],
[
"f_comer_1",
"Tu comes."
],
[
"f_comer_2",
"Ele come."
],
[
"f_comer_3",
"Nós comemos."
],
[
"f_comer_4",
"Eles comem."
],
[
"f_compor_0",
"Eu componho."
],
[
"f_compor_1",
"Tu compões."
],
[
"f_compor_2",
"Ele compõe."
],
[
"f_compor_3",
"Nós compomos."
],
[
"f_compor_4",
"Eles compõem."
],
[
"f_comprar_0",
"Eu compro."
],
[
"f_comprar_1",
"Tu compras."
],
[
"f_comprar_2",
"Ele compra."
],
[
"f_comprar_3",
"Nós compramos."
],
[
"f_comprar_4",
"Eles compram."
],
[
"f_compreender_0",
"Eu compreendo."
],
[
"f_compreender_1",
"Tu compreendes."
],
[
"f_compreender_2",
"Ele compreende."
],
[
"f_compreender_3",
"Nós compreendemos."
],
[
"f_compreender_4",
"Eles compreendem."
],
[
"f_concluir_0",
"Eu concluo."
],
[
"f_concluir_1",
"Tu concluis."
],
[
"f_concluir_2",
"Ele conclui."
],
[
"f_concluir_3",
"Nós concluímos."
],
[
"f_concluir_4",
"Eles concluem."
],
[
"f_conduzir_0",
"Eu conduzo."
],
[
"f_conduzir_1",
"Tu conduzes."
],
[
"f_conduzir_2",
"Ele conduz."
],
[
"f_conduzir_3",
"Nós conduzimos."
],
[
"f_conduzir_4",
"Eles conduzem."
],
[
"f_confessar_0",
"Eu confesso."
],
[
"f_confessar_1",
"Tu confessas."
],
[
"f_confessar_2",
"Ele confessa."
],
[
"f_confessar_3",
"Nós confessamos."
],
[
"f_confessar_4",
"Eles confessam."
],
[
"f_conhecer_0",
"Eu conheço."
],
[
"f_conhecer_1",
"Tu conheces."
],
[
"f_conhecer_2",
"Ele conhece."
],
[
"f_conhecer_3",
"Nós conhecemos."
],
[
"f_conhecer_4",
"Eles conhecem."
],
[
"f_conseguir_0",
"Eu consigo."
],
[
"f_conseguir_1",
"Tu consegues."
],
[
"f_conseguir_2",
"Ele consegue."
],
[
"f_conseguir_3",
"Nós conseguimos."
],
[
"f_conseguir_4",
"Eles conseguem."
],
[
"f_construir_0",
"Eu construo."
],
[
"f_construir_1",
"Tu constróis."
],
[
"f_construir_2",
"Ele constrói."
],
[
"f_construir_3",
"Nós construímos."
],
[
"f_construir_4",
"Eles constroem."
],
[
"f_consumir_0",
"Eu consumo."
],
[
"f_consumir_1",
"Tu consomes."
],
[
"f_consumir_2",
"Ele consome."
],
[
"f_consumir_3",
"Nós consumimos."
],
[
"f_consumir_4",
"Eles consomem."
],
[
"f_contar_0",
"Eu conto."
],
[
"f_contar_1",
"Tu contas."
],
[
"f_contar_2",
"Ele conta."
],
[
"f_contar_3",
"Nós contamos."
],
[
"f_contar_4",
"Eles contam."
],
[
"f_conter_0",
"Eu contenho."
],
[
"f_conter_1",
"Tu conténs."
],
[
"f_conter_2",
"Ele contém."
],
[
"f_conter_3",
"Nós contemos."
],
[
"f_conter_4",
"Eles contêm."
],
[
"f_contradizer_0",
"Eu contradigo."
],
[
"f_contradizer_1",
"Tu contradizes."
],
[
"f_contradizer_2",
"Ele contradiz."
],
[
"f_contradizer_3",
"Nós contradizemos."
],
[
"f_contradizer_4",
"Eles contradizem."
],
[
"f_contribuir_0",
"Eu contribuo."
],
[
"f_contribuir_1",
"Tu contribuis."
],
[
"f_contribuir_2",
"Ele contribui."
],
[
"f_contribuir_3",
"Nós contribuímos."
],
[
"f_contribuir_4",
"Eles contribuem."
],
[
"f_convir_0",
"Eu convenho."
],
[
"f_convir_1",
"Tu convéns."
],
[
"f_convir_2",
"Ele convém."
],
[
"f_convir_3",
"Nós convimos."
],
[
"f_convir_4",
"Eles convêm."
],
[
"f_correr_0",
"Eu corro."
],
[
"f_correr_1",
"Tu corres."
],
[
"f_correr_2",
"Ele corre."
],
[
"f_correr_3",
"Nós corremos."
],
[
"f_correr_4",
"Eles correm."
],
[
"f_corrigir_0",
"Eu corrijo."
],
[
"f_corrigir_1",
"Tu corriges."
],
[
"f_corrigir_2",
"Ele corrige."
],
[
"f_corrigir_3",
"Nós corrigimos."
],
[
"f_corrigir_4",
"Eles corrigem."
],
[
"f_corroer_0",
"Eu corroo."
],
[
"f_corroer_1",
"Tu corróis."
],
[
"f_corroer_2",
"Ele corrói."
],
[
"f_corroer_3",
"Nós corroemos."
],
[
"f_corroer_4",
"Eles corroem."
],
[
"f_cozinhar_0",
"Eu cozinho."
],
[
"f_cozinhar_1",
"Tu cozinhas."
],
[
"f_cozinhar_2",
"Ele cozinha."
],
[
"f_cozinhar_3",
"Nós cozinhamos."
],
[
"f_cozinhar_4",
"Eles cozinham."
],
[
"f_crer_0",
"Eu creio."
],
[
"f_crer_1",
"Tu crês."
],
[
"f_crer_2",
"Ele crê."
],
[
"f_crer_3",
"Nós cremos."
],
[
"f_crer_4",
"Eles creem."
],
[
"f_crescer_0",
"Eu cresço."
],
[
"f_crescer_1",
"Tu cresces."
],
[
"f_crescer_2",
"Ele cresce."
],
[
"f_crescer_3",
"Nós crescemos."
],
[
"f_crescer_4",
"Eles crescem."
],
[
"f_cuspir_0",
"Eu cuspo."
],
[
"f_cuspir_1",
"Tu cospes."
],
[
"f_cuspir_2",
"Ele cospe."
],
[
"f_cuspir_3",
"Nós cuspimos."
],
[
"f_cuspir_4",
"Eles cospem."
],
[
"f_custar_0",
"Eu custo."
],
[
"f_custar_1",
"Tu custas."
],
[
"f_custar_2",
"Ele custa."
],
[
"f_custar_3",
"Nós custamos."
],
[
"f_custar_4",
"Eles custam."
],
[
"f_dancar_0",
"Eu danço."
],
[
"f_dancar_1",
"Tu danças."
],
[
"f_dancar_2",
"Ele dança."
],
[
"f_dancar_3",
"Nós dançamos."
],
[
"f_dancar_4",
"Eles dançam."
],
[
"f_dar_0",
"Eu dou."
],
[
"f_dar_1",
"Tu dás."
],
[
"f_dar_2",
"Ele dá."
],
[
"f_dar_3",
"Nós damos."
],
[
"f_dar_4",
"Eles dão."
],
[
"f_decidir_0",
"Eu decido."
],
[
"f_decidir_1",
"Tu decides."
],
[
"f_decidir_2",
"Ele decide."
],
[
"f_decidir_3",
"Nós decidimos."
],
[
"f_decidir_4",
"Eles decidem."
],
[
"f_deduzir_0",
"Eu deduzo."
],
[
"f_deduzir_1",
"Tu deduzes."
],
[
"f_deduzir_2",
"Ele deduz."
],
[
"f_deduzir_3",
"Nós deduzimos."
],
[
"f_deduzir_4",
"Eles deduzem."
],
[
"f_defender_0",
"Eu defendo."
],
[
"f_defender_1",
"Tu defendes."
],
[
"f_defender_2",
"Ele defende."
],
[
"f_defender_3",
"Nós defendemos."
],
[
"f_defender_4",
"Eles defendem."
],
[
"f_deixar_0",
"Eu deixo."
],
[
"f_deixar_1",
"Tu deixas."
],
[
"f_deixar_2",
"Ele deixa."
],
[
"f_deixar_3",
"Nós deixamos."
],
[
"f_deixar_4",
"Eles deixam."
],
[
"f_depender_0",
"Eu dependo."
],
[
"f_depender_1",
"Tu dependes."
],
[
"f_depender_2",
"Ele depende."
],
[
"f_depender_3",
"Nós dependemos."
],
[
"f_depender_4",
"Eles dependem."
],
[
"f_descer_0",
"Eu desço."
],
[
"f_descer_1",
"Tu desces."
],
[
"f_descer_2",
"Ele desce."
],
[
"f_descer_3",
"Nós descemos."
],
[
"f_descer_4",
"Eles descem."
],
[
"f_descobrir_0",
"Eu descubro."
],
[
"f_descobrir_1",
"Tu descobres."
],
[
"f_descobrir_2",
"Ele descobre."
],
[
"f_descobrir_3",
"Nós descobrimos."
],
[
"f_descobrir_4",
"Eles descobrem."
],
[
"f_desfazer_0",
"Eu desfaço."
],
[
"f_desfazer_1",
"Tu desfazes."
],
[
"f_desfazer_2",
"Ele desfaz."
],
[
"f_desfazer_3",
"Nós desfazemos."
],
[
"f_desfazer_4",
"Eles desfazem."
],
[
"f_despedir_0",
"Eu despeço."
],
[
"f_despedir_1",
"Tu despedes."
],
[
"f_despedir_2",
"Ele despede."
],
[
"f_despedir_3",
"Nós despedimos."
],
[
"f_despedir_4",
"Eles despedem."
],
[
"f_despertar_0",
"Eu desperto."
],
[
"f_despertar_1",
"Tu despertas."
],
[
"f_despertar_2",
"Ele desperta."
],
[
"f_despertar_3",
"Nós despertamos."
],
[
"f_despertar_4",
"Eles despertam."
],
[
"f_despir_0",
"Eu dispo."
],
[
"f_despir_1",
"Tu despes."
],
[
"f_despir_2",
"Ele despe."
],
[
"f_despir_3",
"Nós despimos."
],
[
"f_despir_4",
"Eles despem."
],
[
"f_destruir_0",
"Eu destruo."
],
[
"f_destruir_1",
"Tu destróis."
],
[
"f_destruir_2",
"Ele destrói."
],
[
"f_destruir_3",
"Nós destruímos."
],
[
"f_destruir_4",
"Eles destroem."
],
[
"f_deter_0",
"Eu detenho."
],
[
"f_deter_1",
"Tu deténs."
],
[
"f_deter_2",
"Ele detém."
],
[
"f_deter_3",
"Nós detemos."
],
[
"f_deter_4",
"Eles detêm."
],
[
"f_devolver_0",
"Eu devolvo."
],
[
"f_devolver_1",
"Tu devolves."
],
[
"f_devolver_2",
"Ele devolve."
],
[
"f_devolver_3",
"Nós devolvemos."
],
[
"f_devolver_4",
"Eles devolvem."
],
[
"f_diminuir_0",
"Eu diminuo."
],
[
"f_diminuir_1",
"Tu diminuis."
],
[
"f_diminuir_2",
"Ele diminui."
],
[
"f_diminuir_3",
"Nós diminuímos."
],
[
"f_diminuir_4",
"Eles diminuem."
],
[
"f_dirigir_0",
"Eu dirijo."
],
[
"f_dirigir_1",
"Tu diriges."
],
[
"f_dirigir_2",
"Ele dirige."
],
[
"f_dirigir_3",
"Nós dirigimos."
],
[
"f_dirigir_4",
"Eles dirigem."
],
[
"f_discutir_0",
"Eu discuto."
],
[
"f_discutir_1",
"Tu discutes."
],
[
"f_discutir_2",
"Ele discute."
],
[
"f_discutir_3",
"Nós discutimos."
],
[
"f_discutir_4",
"Eles discutem."
],
[
"f_dispor_0",
"Eu disponho."
],
[
"f_dispor_1",
"Tu dispões."
],
[
"f_dispor_2",
"Ele dispõe."
],
[
"f_dispor_3",
"Nós dispomos."
],
[
"f_dispor_4",
"Eles dispõem."
],
[
"f_distrair_0",
"Eu distraio."
],
[
"f_distrair_1",
"Tu distrais."
],
[
"f_distrair_2",
"Ele distrai."
],
[
"f_distrair_3",
"Nós distraímos."
],
[
"f_distrair_4",
"Eles distraem."
],
[
"f_distribuir_0",
"Eu distribuo."
],
[
"f_distribuir_1",
"Tu distribuis."
],
[
"f_distribuir_2",
"Ele distribui."
],
[
"f_distribuir_3",
"Nós distribuímos."
],
[
"f_distribuir_4",
"Eles distribuem."
],
[
"f_divertir_0",
"Eu divirto."
],
[
"f_divertir_1",
"Tu divertes."
],
[
"f_divertir_2",
"Ele diverte."
],
[
"f_divertir_3",
"Nós divertimos."
],
[
"f_divertir_4",
"Eles divertem."
],
[
"f_dividir_0",
"Eu divido."
],
[
"f_dividir_1",
"Tu divides."
],
[
"f_dividir_2",
"Ele divide."
],
[
"f_dividir_3",
"Nós dividimos."
],
[
"f_dividir_4",
"Eles dividem."
],
[
"f_dizer_0",
"Eu digo."
],
[
"f_dizer_1",
"Tu dizes."
],
[
"f_dizer_2",
"Ele diz."
],
[
"f_dizer_3",
"Nós dizemos."
],
[
"f_dizer_4",
"Eles dizem."
],
[
"f_dormir_0",
"Eu durmo."
],
[
"f_dormir_1",
"Tu dormes."
],
[
"f_dormir_2",
"Ele dorme."
],
[
"f_dormir_3",
"Nós dormimos."
],
[
"f_dormir_4",
"Eles dormem."
],
[
"f_eleger_0",
"Eu elejo."
],
[
"f_eleger_1",
"Tu eleges."
],
[
"f_eleger_2",
"Ele elege."
],
[
"f_eleger_3",
"Nós elegemos."
],
[
"f_eleger_4",
"Eles elegem."
],
[
"f_encontrar_0",
"Eu encontro."
],
[
"f_encontrar_1",
"Tu encontras."
],
[
"f_encontrar_2",
"Ele encontra."
],
[
"f_encontrar_3",
"Nós encontramos."
],
[
"f_encontrar_4",
"Eles encontram."
],
[
"f_engolir_0",
"Eu engulo."
],
[
"f_engolir_1",
"Tu engoles."
],
[
"f_engolir_2",
"Ele engole."
],
[
"f_engolir_3",
"Nós engolimos."
],
[
"f_engolir_4",
"Eles engolem."
],
[
"f_entender_0",
"Eu entendo."
],
[
"f_entender_1",
"Tu entendes."
],
[
"f_entender_2",
"Ele entende."
],
[
"f_entender_3",
"Nós entendemos."
],
[
"f_entender_4",
"Eles entendem."
],
[
"f_entrar_0",
"Eu entro."
],
[
"f_entrar_1",
"Tu entras."
],
[
"f_entrar_2",
"Ele entra."
],
[
"f_entrar_3",
"Nós entramos."
],
[
"f_entrar_4",
"Eles entram."
],
[
"f_entreter_0",
"Eu entretenho."
],
[
"f_entreter_1",
"Tu entreténs."
],
[
"f_entreter_2",
"Ele entretém."
],
[
"f_entreter_3",
"Nós entretemos."
],
[
"f_entreter_4",
"Eles entretêm."
],
[
"f_entupir_0",
"Eu entupo."
],
[
"f_entupir_1",
"Tu entopes."
],
[
"f_entupir_2",
"Ele entope."
],
[
"f_entupir_3",
"Nós entupimos."
],
[
"f_entupir_4",
"Eles entopem."
],
[
"f_escolher_0",
"Eu escolho."
],
[
"f_escolher_1",
"Tu escolhes."
],
[
"f_escolher_2",
"Ele escolhe."
],
[
"f_escolher_3",
"Nós escolhemos."
],
[
"f_escolher_4",
"Eles escolhem."
],
[
"f_escrever_0",
"Eu escrevo."
],
[
"f_escrever_1",
"Tu escreves."
],
[
"f_escrever_2",
"Ele escreve."
],
[
"f_escrever_3",
"Nós escrevemos."
],
[
"f_escrever_4",
"Eles escrevem."
],
[
"f_esperar_0",
"Eu espero."
],
[
"f_esperar_1",
"Tu esperas."
],
[
"f_esperar_2",
"Ele espera."
],
[
"f_esperar_3",
"Nós esperamos."
],
[
"f_esperar_4",
"Eles esperam."
],
[
"f_esquecer_0",
"Eu esqueço."
],
[
"f_esquecer_1",
"Tu esqueces."
],
[
"f_esquecer_2",
"Ele esquece."
],
[
"f_esquecer_3",
"Nós esquecemos."
],
[
"f_esquecer_4",
"Eles esquecem."
],
[
"f_estabelecer_0",
"Eu estabeleço."
],
[
"f_estabelecer_1",
"Tu estabeleces."
],
[
"f_estabelecer_2",
"Ele estabelece."
],
[
"f_estabelecer_3",
"Nós estabelecemos."
],
[
"f_estabelecer_4",
"Eles estabelecem."
],
[
"f_estar_0",
"Eu estou."
],
[
"f_estar_1",
"Tu estás."
],
[
"f_estar_2",
"Ele está."
],
[
"f_estar_3",
"Nós estamos."
],
[
"f_estar_4",
"Eles estão."
],
[
"f_estrear_0",
"Eu estreio."
],
[
"f_estrear_1",
"Tu estreias."
],
[
"f_estrear_2",
"Ele estreia."
],
[
"f_estrear_3",
"Nós estreamos."
],
[
"f_estrear_4",
"Eles estreiam."
],
[
"f_estudar_0",
"Eu estudo."
],
[
"f_estudar_1",
"Tu estudas."
],
[
"f_estudar_2",
"Ele estuda."
],
[
"f_estudar_3",
"Nós estudamos."
],
[
"f_estudar_4",
"Eles estudam."
],
[
"f_exigir_0",
"Eu exijo."
],
[
"f_exigir_1",
"Tu exiges."
],
[
"f_exigir_2",
"Ele exige."
],
[
"f_exigir_3",
"Nós exigimos."
],
[
"f_exigir_4",
"Eles exigem."
],
[
"f_existir_0",
"Eu existo."
],
[
"f_existir_1",
"Tu existes."
],
[
"f_existir_2",
"Ele existe."
],
[
"f_existir_3",
"Nós existimos."
],
[
"f_existir_4",
"Eles existem."
],
[
"f_expor_0",
"Eu exponho."
],
[
"f_expor_1",
"Tu expões."
],
[
"f_expor_2",
"Ele expõe."
],
[
"f_expor_3",
"Nós expomos."
],
[
"f_expor_4",
"Eles expõem."
],
[
"f_falar_0",
"Eu falo."
],
[
"f_falar_1",
"Tu falas."
],
[
"f_falar_2",
"Ele fala."
],
[
"f_falar_3",
"Nós falamos."
],
[
"f_falar_4",
"Eles falam."
],
[
"f_fazer_0",
"Eu faço."
],
[
"f_fazer_1",
"Tu fazes."
],
[
"f_fazer_2",
"Ele faz."
],
[
"f_fazer_3",
"Nós fazemos."
],
[
"f_fazer_4",
"Eles fazem."
],
[
"f_fechar_0",
"Eu fecho."
],
[
"f_fechar_1",
"Tu fechas."
],
[
"f_fechar_2",
"Ele fecha."
],
[
"f_fechar_3",
"Nós fechamos."
],
[
"f_fechar_4",
"Eles fecham."
],
[
"f_ferir_0",
"Eu firo."
],
[
"f_ferir_1",
"Tu feres."
],
[
"f_ferir_2",
"Ele fere."
],
[
"f_ferir_3",
"Nós ferimos."
],
[
"f_ferir_4",
"Eles ferem."
],
[
"f_ficar_0",
"Eu fico."
],
[
"f_ficar_1",
"Tu ficas."
],
[
"f_ficar_2",
"Ele fica."
],
[
"f_ficar_3",
"Nós ficamos."
],
[
"f_ficar_4",
"Eles ficam."
],
[
"f_fingir_0",
"Eu finjo."
],
[
"f_fingir_1",
"Tu finges."
],
[
"f_fingir_2",
"Ele finge."
],
[
"f_fingir_3",
"Nós fingimos."
],
[
"f_fingir_4",
"Eles fingem."
],
[
"f_fugir_0",
"Eu fujo."
],
[
"f_fugir_1",
"Tu foges."
],
[
"f_fugir_2",
"Ele foge."
],
[
"f_fugir_3",
"Nós fugimos."
],
[
"f_fugir_4",
"Eles fogem."
],
[
"f_garantir_0",
"Eu garanto."
],
[
"f_garantir_1",
"Tu garantes."
],
[
"f_garantir_2",
"Ele garante."
],
[
"f_garantir_3",
"Nós garantimos."
],
[
"f_garantir_4",
"Eles garantem."
],
[
"f_gostar_0",
"Eu gosto."
],
[
"f_gostar_1",
"Tu gostas."
],
[
"f_gostar_2",
"Ele gosta."
],
[
"f_gostar_3",
"Nós gostamos."
],
[
"f_gostar_4",
"Eles gostam."
],
[
"f_haver_0",
"Eu hei."
],
[
"f_haver_1",
"Tu hás."
],
[
"f_haver_2",
"Ele há."
],
[
"f_haver_3",
"Nós havemos."
],
[
"f_haver_4",
"Eles hão."
],
[
"f_impedir_0",
"Eu impeço."
],
[
"f_impedir_1",
"Tu impedes."
],
[
"f_impedir_2",
"Ele impede."
],
[
"f_impedir_3",
"Nós impedimos."
],
[
"f_impedir_4",
"Eles impedem."
],
[
"f_impor_0",
"Eu imponho."
],
[
"f_impor_1",
"Tu impões."
],
[
"f_impor_2",
"Ele impõe."
],
[
"f_impor_3",
"Nós impomos."
],
[
"f_impor_4",
"Eles impõem."
],
[
"f_imprimir_0",
"Eu imprimo."
],
[
"f_imprimir_1",
"Tu imprimes."
],
[
"f_imprimir_2",
"Ele imprime."
],
[
"f_imprimir_3",
"Nós imprimimos."
],
[
"f_imprimir_4",
"Eles imprimem."
],
[
"f_incendiar_0",
"Eu incendeio."
],
[
"f_incendiar_1",
"Tu incendeias."
],
[
"f_incendiar_2",
"Ele incendeia."
],
[
"f_incendiar_3",
"Nós incendiamos."
],
[
"f_incendiar_4",
"Eles incendeiam."
],
[
"f_incluir_0",
"Eu incluo."
],
[
"f_incluir_1",
"Tu incluis."
],
[
"f_incluir_2",
"Ele inclui."
],
[
"f_incluir_3",
"Nós incluímos."
],
[
"f_incluir_4",
"Eles incluem."
],
[
"f_insistir_0",
"Eu insisto."
],
[
"f_insistir_1",
"Tu insistes."
],
[
"f_insistir_2",
"Ele insiste."
],
[
"f_insistir_3",
"Nós insistimos."
],
[
"f_insistir_4",
"Eles insistem."
],
[
"f_intervir_0",
"Eu intervenho."
],
[
"f_intervir_1",
"Tu intervéns."
],
[
"f_intervir_2",
"Ele intervém."
],
[
"f_intervir_3",
"Nós intervimos."
],
[
"f_intervir_4",
"Eles intervêm."
],
[
"f_introduzir_0",
"Eu introduzo."
],
[
"f_introduzir_1",
"Tu introduzes."
],
[
"f_introduzir_2",
"Ele introduz."
],
[
"f_introduzir_3",
"Nós introduzimos."
],
[
"f_introduzir_4",
"Eles introduzem."
],
[
"f_investir_0",
"Eu invisto."
],
[
"f_investir_1",
"Tu investes."
],
[
"f_investir_2",
"Ele investe."
],
[
"f_investir_3",
"Nós investimos."
],
[
"f_investir_4",
"Eles investem."
],
[
"f_ir_0",
"Eu vou."
],
[
"f_ir_1",
"Tu vais."
],
[
"f_ir_2",
"Ele vai."
],
[
"f_ir_3",
"Nós vamos."
],
[
"f_ir_4",
"Eles vão."
],
[
"f_jantar_0",
"Eu janto."
],
[
"f_jantar_1",
"Tu jantas."
],
[
"f_jantar_2",
"Ele janta."
],
[
"f_jantar_3",
"Nós jantamos."
],
[
"f_jantar_4",
"Eles jantam."
],
[
"f_jogar_0",
"Eu jogo."
],
[
"f_jogar_1",
"Tu jogas."
],
[
"f_jogar_2",
"Ele joga."
],
[
"f_jogar_3",
"Nós jogamos."
],
[
"f_jogar_4",
"Eles jogam."
],
[
"f_lavar_0",
"Eu lavo."
],
[
"f_lavar_1",
"Tu lavas."
],
[
"f_lavar_2",
"Ele lava."
],
[
"f_lavar_3",
"Nós lavamos."
],
[
"f_lavar_4",
"Eles lavam."
],
[
"f_ler_0",
"Eu leio."
],
[
"f_ler_1",
"Tu lês."
],
[
"f_ler_2",
"Ele lê."
],
[
"f_ler_3",
"Nós lemos."
],
[
"f_ler_4",
"Eles leem."
],
[
"f_levar_0",
"Eu levo."
],
[
"f_levar_1",
"Tu levas."
],
[
"f_levar_2",
"Ele leva."
],
[
"f_levar_3",
"Nós levamos."
],
[
"f_levar_4",
"Eles levam."
],
[
"f_ligar_0",
"Eu ligo."
],
[
"f_ligar_1",
"Tu ligas."
],
[
"f_ligar_2",
"Ele liga."
],
[
"f_ligar_3",
"Nós ligamos."
],
[
"f_ligar_4",
"Eles ligam."
],
[
"f_limpar_0",
"Eu limpo."
],
[
"f_limpar_1",
"Tu limpas."
],
[
"f_limpar_2",
"Ele limpa."
],
[
"f_limpar_3",
"Nós limpamos."
],
[
"f_limpar_4",
"Eles limpam."
],
[
"f_manter_0",
"Eu mantenho."
],
[
"f_manter_1",
"Tu manténs."
],
[
"f_manter_2",
"Ele mantém."
],
[
"f_manter_3",
"Nós mantemos."
],
[
"f_manter_4",
"Eles mantêm."
],
[
"f_mediar_0",
"Eu medeio."
],
[
"f_mediar_1",
"Tu medeias."
],
[
"f_mediar_2",
"Ele medeia."
],
[
"f_mediar_3",
"Nós mediamos."
],
[
"f_mediar_4",
"Eles medeiam."
],
[
"f_medir_0",
"Eu meço."
],
[
"f_medir_1",
"Tu medes."
],
[
"f_medir_2",
"Ele mede."
],
[
"f_medir_3",
"Nós medimos."
],
[
"f_medir_4",
"Eles medem."
],
[
"f_mentir_0",
"Eu minto."
],
[
"f_mentir_1",
"Tu mentes."
],
[
"f_mentir_2",
"Ele mente."
],
[
"f_mentir_3",
"Nós mentimos."
],
[
"f_mentir_4",
"Eles mentem."
],
[
"f_merecer_0",
"Eu mereço."
],
[
"f_merecer_1",
"Tu mereces."
],
[
"f_merecer_2",
"Ele merece."
],
[
"f_merecer_3",
"Nós merecemos."
],
[
"f_merecer_4",
"Eles merecem."
],
[
"f_meter_0",
"Eu meto."
],
[
"f_meter_1",
"Tu metes."
],
[
"f_meter_2",
"Ele mete."
],
[
"f_meter_3",
"Nós metemos."
],
[
"f_meter_4",
"Eles metem."
],
[
"f_moer_0",
"Eu moo."
],
[
"f_moer_1",
"Tu móis."
],
[
"f_moer_2",
"Ele mói."
],
[
"f_moer_3",
"Nós moemos."
],
[
"f_moer_4",
"Eles moem."
],
[
"f_morar_0",
"Eu moro."
],
[
"f_morar_1",
"Tu moras."
],
[
"f_morar_2",
"Ele mora."
],
[
"f_morar_3",
"Nós moramos."
],
[
"f_morar_4",
"Eles moram."
],
[
"f_mostrar_0",
"Eu mostro."
],
[
"f_mostrar_1",
"Tu mostras."
],
[
"f_mostrar_2",
"Ele mostra."
],
[
"f_mostrar_3",
"Nós mostramos."
],
[
"f_mostrar_4",
"Eles mostram."
],
[
"f_mover_0",
"Eu movo."
],
[
"f_mover_1",
"Tu moves."
],
[
"f_mover_2",
"Ele move."
],
[
"f_mover_3",
"Nós movemos."
],
[
"f_mover_4",
"Eles movem."
],
[
"f_mudar_0",
"Eu mudo."
],
[
"f_mudar_1",
"Tu mudas."
],
[
"f_mudar_2",
"Ele muda."
],
[
"f_mudar_3",
"Nós mudamos."
],
[
"f_mudar_4",
"Eles mudam."
],
[
"f_nadar_0",
"Eu nado."
],
[
"f_nadar_1",
"Tu nadas."
],
[
"f_nadar_2",
"Ele nada."
],
[
"f_nadar_3",
"Nós nadamos."
],
[
"f_nadar_4",
"Eles nadam."
],
[
"f_nascer_0",
"Eu nasço."
],
[
"f_nascer_1",
"Tu nasces."
],
[
"f_nascer_2",
"Ele nasce."
],
[
"f_nascer_3",
"Nós nascemos."
],
[
"f_nascer_4",
"Eles nascem."
],
[
"f_negar_0",
"Eu nego."
],
[
"f_negar_1",
"Tu negas."
],
[
"f_negar_2",
"Ele nega."
],
[
"f_negar_3",
"Nós negamos."
],
[
"f_negar_4",
"Eles negam."
],
[
"f_nomear_0",
"Eu nomeio."
],
[
"f_nomear_1",
"Tu nomeias."
],
[
"f_nomear_2",
"Ele nomeia."
],
[
"f_nomear_3",
"Nós nomeamos."
],
[
"f_nomear_4",
"Eles nomeiam."
],
[
"f_obedecer_0",
"Eu obedeço."
],
[
"f_obedecer_1",
"Tu obedeces."
],
[
"f_obedecer_2",
"Ele obedece."
],
[
"f_obedecer_3",
"Nós obedecemos."
],
[
"f_obedecer_4",
"Eles obedecem."
],
[
"f_obter_0",
"Eu obtenho."
],
[
"f_obter_1",
"Tu obténs."
],
[
"f_obter_2",
"Ele obtém."
],
[
"f_obter_3",
"Nós obtemos."
],
[
"f_obter_4",
"Eles obtêm."
],
[
"f_odiar_0",
"Eu odeio."
],
[
"f_odiar_1",
"Tu odeias."
],
[
"f_odiar_2",
"Ele odeia."
],
[
"f_odiar_3",
"Nós odiamos."
],
[
"f_odiar_4",
"Eles odeiam."
],
[
"f_oferecer_0",
"Eu ofereço."
],
[
"f_oferecer_1",
"Tu ofereces."
],
[
"f_oferecer_2",
"Ele oferece."
],
[
"f_oferecer_3",
"Nós oferecemos."
],
[
"f_oferecer_4",
"Eles oferecem."
],
[
"f_omitir_0",
"Eu omito."
],
[
"f_omitir_1",
"Tu omites."
],
[
"f_omitir_2",
"Ele omite."
],
[
"f_omitir_3",
"Nós omitimos."
],
[
"f_omitir_4",
"Eles omitem."
],
[
"f_ouvir_0",
"Eu ouço."
],
[
"f_ouvir_1",
"Tu ouves."
],
[
"f_ouvir_2",
"Ele ouve."
],
[
"f_ouvir_3",
"Nós ouvimos."
],
[
"f_ouvir_4",
"Eles ouvem."
],
[
"f_pagar_0",
"Eu pago."
],
[
"f_pagar_1",
"Tu pagas."
],
[
"f_pagar_2",
"Ele paga."
],
[
"f_pagar_3",
"Nós pagamos."
],
[
"f_pagar_4",
"Eles pagam."
],
[
"f_parecer_0",
"Eu pareço."
],
[
"f_parecer_1",
"Tu pareces."
],
[
"f_parecer_2",
"Ele parece."
],
[
"f_parecer_3",
"Nós parecemos."
],
[
"f_parecer_4",
"Eles parecem."
],
[
"f_partir_0",
"Eu parto."
],
[
"f_partir_1",
"Tu partes."
],
[
"f_partir_2",
"Ele parte."
],
[
"f_partir_3",
"Nós partimos."
],
[
"f_partir_4",
"Eles partem."
],
[
"f_passear_0",
"Eu passeio."
],
[
"f_passear_1",
"Tu passeias."
],
[
"f_passear_2",
"Ele passeia."
],
[
"f_passear_3",
"Nós passeamos."
],
[
"f_passear_4",
"Eles passeiam."
],
[
"f_pedir_0",
"Eu peço."
],
[
"f_pedir_1",
"Tu pedes."
],
[
"f_pedir_2",
"Ele pede."
],
[
"f_pedir_3",
"Nós pedimos."
],
[
"f_pedir_4",
"Eles pedem."
],
[
"f_pensar_0",
"Eu penso."
],
[
"f_pensar_1",
"Tu pensas."
],
[
"f_pensar_2",
"Ele pensa."
],
[
"f_pensar_3",
"Nós pensamos."
],
[
"f_pensar_4",
"Eles pensam."
],
[
"f_pentear_0",
"Eu penteio."
],
[
"f_pentear_1",
"Tu penteias."
],
[
"f_pentear_2",
"Ele penteia."
],
[
"f_pentear_3",
"Nós penteamos."
],
[
"f_pentear_4",
"Eles penteiam."
],
[
"f_perder_0",
"Eu perco."
],
[
"f_perder_1",
"Tu perdes."
],
[
"f_perder_2",
"Ele perde."
],
[
"f_perder_3",
"Nós perdemos."
],
[
"f_perder_4",
"Eles perdem."
],
[
"f_perguntar_0",
"Eu pergunto."
],
[
"f_perguntar_1",
"Tu perguntas."
],
[
"f_perguntar_2",
"Ele pergunta."
],
[
"f_perguntar_3",
"Nós perguntamos."
],
[
"f_perguntar_4",
"Eles perguntam."
],
[
"f_permitir_0",
"Eu permito."
],
[
"f_permitir_1",
"Tu permites."
],
[
"f_permitir_2",
"Ele permite."
],
[
"f_permitir_3",
"Nós permitimos."
],
[
"f_permitir_4",
"Eles permitem."
],
[
"f_poder_0",
"Eu posso."
],
[
"f_poder_1",
"Tu podes."
],
[
"f_poder_2",
"Ele pode."
],
[
"f_poder_3",
"Nós podemos."
],
[
"f_poder_4",
"Eles podem."
],
[
"f_poluir_0",
"Eu poluo."
],
[
"f_poluir_1",
"Tu poluis."
],
[
"f_poluir_2",
"Ele polui."
],
[
"f_poluir_3",
"Nós poluímos."
],
[
"f_poluir_4",
"Eles poluem."
],
[
"f_por_0",
"Eu ponho."
],
[
"f_por_1",
"Tu pões."
],
[
"f_por_2",
"Ele põe."
],
[
"f_por_3",
"Nós pomos."
],
[
"f_por_4",
"Eles põem."
],
[
"f_possuir_0",
"Eu possuo."
],
[
"f_possuir_1",
"Tu possuis."
],
[
"f_possuir_2",
"Ele possui."
],
[
"f_possuir_3",
"Nós possuímos."
],
[
"f_possuir_4",
"Eles possuem."
],
[
"f_precisar_0",
"Eu preciso."
],
[
"f_precisar_1",
"Tu precisas."
],
[
"f_precisar_2",
"Ele precisa."
],
[
"f_precisar_3",
"Nós precisamos."
],
[
"f_precisar_4",
"Eles precisam."
],
[
"f_preferir_0",
"Eu prefiro."
],
[
"f_preferir_1",
"Tu preferes."
],
[
"f_preferir_2",
"Ele prefere."
],
[
"f_preferir_3",
"Nós preferimos."
],
[
"f_preferir_4",
"Eles preferem."
],
[
"f_prever_0",
"Eu prevejo."
],
[
"f_prever_1",
"Tu prevês."
],
[
"f_prever_2",
"Ele prevê."
],
[
"f_prever_3",
"Nós prevemos."
],
[
"f_prever_4",
"Eles preveem."
],
[
"f_procurar_0",
"Eu procuro."
],
[
"f_procurar_1",
"Tu procuras."
],
[
"f_procurar_2",
"Ele procura."
],
[
"f_procurar_3",
"Nós procuramos."
],
[
"f_procurar_4",
"Eles procuram."
],
[
"f_produzir_0",
"Eu produzo."
],
[
"f_produzir_1",
"Tu produzes."
],
[
"f_produzir_2",
"Ele produz."
],
[
"f_produzir_3",
"Nós produzimos."
],
[
"f_produzir_4",
"Eles produzem."
],
[
"f_propor_0",
"Eu proponho."
],
[
"f_propor_1",
"Tu propões."
],
[
"f_propor_2",
"Ele propõe."
],
[
"f_propor_3",
"Nós propomos."
],
[
"f_propor_4",
"Eles propõem."
],
[
"f_proteger_0",
"Eu protejo."
],
[
"f_proteger_1",
"Tu proteges."
],
[
"f_proteger_2",
"Ele protege."
],
[
"f_proteger_3",
"Nós protegemos."
],
[
"f_proteger_4",
"Eles protegem."
],
[
"f_provar_0",
"Eu provo."
],
[
"f_provar_1",
"Tu provas."
],
[
"f_provar_2",
"Ele prova."
],
[
"f_provar_3",
"Nós provamos."
],
[
"f_provar_4",
"Eles provam."
],
[
"f_querer_0",
"Eu quero."
],
[
"f_querer_1",
"Tu queres."
],
[
"f_querer_2",
"Ele quer."
],
[
"f_querer_3",
"Nós queremos."
],
[
"f_querer_4",
"Eles querem."
],
[
"f_reagir_0",
"Eu reajo."
],
[
"f_reagir_1",
"Tu reages."
],
[
"f_reagir_2",
"Ele reage."
],
[
"f_reagir_3",
"Nós reagimos."
],
[
"f_reagir_4",
"Eles reagem."
],
[
"f_recear_0",
"Eu receio."
],
[
"f_recear_1",
"Tu receias."
],
[
"f_recear_2",
"Ele receia."
],
[
"f_recear_3",
"Nós receamos."
],
[
"f_recear_4",
"Eles receiam."
],
[
"f_receber_0",
"Eu recebo."
],
[
"f_receber_1",
"Tu recebes."
],
[
"f_receber_2",
"Ele recebe."
],
[
"f_receber_3",
"Nós recebemos."
],
[
"f_receber_4",
"Eles recebem."
],
[
"f_recomendar_0",
"Eu recomendo."
],
[
"f_recomendar_1",
"Tu recomendas."
],
[
"f_recomendar_2",
"Ele recomenda."
],
[
"f_recomendar_3",
"Nós recomendamos."
],
[
"f_recomendar_4",
"Eles recomendam."
],
[
"f_recordar_0",
"Eu recordo."
],
[
"f_recordar_1",
"Tu recordas."
],
[
"f_recordar_2",
"Ele recorda."
],
[
"f_recordar_3",
"Nós recordamos."
],
[
"f_recordar_4",
"Eles recordam."
],
[
"f_reduzir_0",
"Eu reduzo."
],
[
"f_reduzir_1",
"Tu reduzes."
],
[
"f_reduzir_2",
"Ele reduz."
],
[
"f_reduzir_3",
"Nós reduzimos."
],
[
"f_reduzir_4",
"Eles reduzem."
],
[
"f_refazer_0",
"Eu refaço."
],
[
"f_refazer_1",
"Tu refazes."
],
[
"f_refazer_2",
"Ele refaz."
],
[
"f_refazer_3",
"Nós refazemos."
],
[
"f_refazer_4",
"Eles refazem."
],
[
"f_referir_0",
"Eu refiro."
],
[
"f_referir_1",
"Tu referes."
],
[
"f_referir_2",
"Ele refere."
],
[
"f_referir_3",
"Nós referimos."
],
[
"f_referir_4",
"Eles referem."
],
[
"f_reler_0",
"Eu releio."
],
[
"f_reler_1",
"Tu relês."
],
[
"f_reler_2",
"Ele relê."
],
[
"f_reler_3",
"Nós relemos."
],
[
"f_reler_4",
"Eles releem."
],
[
"f_remediar_0",
"Eu remedeio."
],
[
"f_remediar_1",
"Tu remedeias."
],
[
"f_remediar_2",
"Ele remedeia."
],
[
"f_remediar_3",
"Nós remediamos."
],
[
"f_remediar_4",
"Eles remedeiam."
],
[
"f_repetir_0",
"Eu repito."
],
[
"f_repetir_1",
"Tu repetes."
],
[
"f_repetir_2",
"Ele repete."
],
[
"f_repetir_3",
"Nós repetimos."
],
[
"f_repetir_4",
"Eles repetem."
],
[
"f_resistir_0",
"Eu resisto."
],
[
"f_resistir_1",
"Tu resistes."
],
[
"f_resistir_2",
"Ele resiste."
],
[
"f_resistir_3",
"Nós resistimos."
],
[
"f_resistir_4",
"Eles resistem."
],
[
"f_responder_0",
"Eu respondo."
],
[
"f_responder_1",
"Tu respondes."
],
[
"f_responder_2",
"Ele responde."
],
[
"f_responder_3",
"Nós respondemos."
],
[
"f_responder_4",
"Eles respondem."
],
[
"f_reter_0",
"Eu retenho."
],
[
"f_reter_1",
"Tu reténs."
],
[
"f_reter_2",
"Ele retém."
],
[
"f_reter_3",
"Nós retemos."
],
[
"f_reter_4",
"Eles retêm."
],
[
"f_rever_0",
"Eu revejo."
],
[
"f_rever_1",
"Tu revês."
],
[
"f_rever_2",
"Ele revê."
],
[
"f_rever_3",
"Nós revemos."
],
[
"f_rever_4",
"Eles reveem."
],
[
"f_rir_0",
"Eu rio."
],
[
"f_rir_1",
"Tu ris."
],
[
"f_rir_2",
"Ele ri."
],
[
"f_rir_3",
"Nós rimos."
],
[
"f_rir_4",
"Eles riem."
],
[
"f_roer_0",
"Eu roo."
],
[
"f_roer_1",
"Tu róis."
],
[
"f_roer_2",
"Ele rói."
],
[
"f_roer_3",
"Nós roemos."
],
[
"f_roer_4",
"Eles roem."
],
[
"f_saber_0",
"Eu sei."
],
[
"f_saber_1",
"Tu sabes."
],
[
"f_saber_2",
"Ele sabe."
],
[
"f_saber_3",
"Nós sabemos."
],
[
"f_saber_4",
"Eles sabem."
],
[
"f_sacudir_0",
"Eu sacudo."
],
[
"f_sacudir_1",
"Tu sacodes."
],
[
"f_sacudir_2",
"Ele sacode."
],
[
"f_sacudir_3",
"Nós sacudimos."
],
[
"f_sacudir_4",
"Eles sacodem."
],
[
"f_sair_0",
"Eu saio."
],
[
"f_sair_1",
"Tu sais."
],
[
"f_sair_2",
"Ele sai."
],
[
"f_sair_3",
"Nós saímos."
],
[
"f_sair_4",
"Eles saem."
],
[
"f_satisfazer_0",
"Eu satisfaço."
],
[
"f_satisfazer_1",
"Tu satisfazes."
],
[
"f_satisfazer_2",
"Ele satisfaz."
],
[
"f_satisfazer_3",
"Nós satisfazemos."
],
[
"f_satisfazer_4",
"Eles satisfazem."
],
[
"f_seguir_0",
"Eu sigo."
],
[
"f_seguir_1",
"Tu segues."
],
[
"f_seguir_2",
"Ele segue."
],
[
"f_seguir_3",
"Nós seguimos."
],
[
"f_seguir_4",
"Eles seguem."
],
[
"f_semear_0",
"Eu semeio."
],
[
"f_semear_1",
"Tu semeias."
],
[
"f_semear_2",
"Ele semeia."
],
[
"f_semear_3",
"Nós semeamos."
],
[
"f_semear_4",
"Eles semeiam."
],
[
"f_sentar_0",
"Eu sento."
],
[
"f_sentar_1",
"Tu sentas."
],
[
"f_sentar_2",
"Ele senta."
],
[
"f_sentar_3",
"Nós sentamos."
],
[
"f_sentar_4",
"Eles sentam."
],
[
"f_sentir_0",
"Eu sinto."
],
[
"f_sentir_1",
"Tu sentes."
],
[
"f_sentir_2",
"Ele sente."
],
[
"f_sentir_3",
"Nós sentimos."
],
[
"f_sentir_4",
"Eles sentem."
],
[
"f_ser_0",
"Eu sou."
],
[
"f_ser_1",
"Tu és."
],
[
"f_ser_2",
"Ele é."
],
[
"f_ser_3",
"Nós somos."
],
[
"f_ser_4",
"Eles são."
],
[
"f_servir_0",
"Eu sirvo."
],
[
"f_servir_1",
"Tu serves."
],
[
"f_servir_2",
"Ele serve."
],
[
"f_servir_3",
"Nós servimos."
],
[
"f_servir_4",
"Eles servem."
],
[
"f_sonhar_0",
"Eu sonho."
],
[
"f_sonhar_1",
"Tu sonhas."
],
[
"f_sonhar_2",
"Ele sonha."
],
[
"f_sonhar_3",
"Nós sonhamos."
],
[
"f_sonhar_4",
"Eles sonham."
],
[
"f_sorrir_0",
"Eu sorrio."
],
[
"f_sorrir_1",
"Tu sorris."
],
[
"f_sorrir_2",
"Ele sorri."
],
[
"f_sorrir_3",
"Nós sorrimos."
],
[
"f_sorrir_4",
"Eles sorriem."
],
[
"f_subir_0",
"Eu subo."
],
[
"f_subir_1",
"Tu sobes."
],
[
"f_subir_2",
"Ele sobe."
],
[
"f_subir_3",
"Nós subimos."
],
[
"f_subir_4",
"Eles sobem."
],
[
"f_substituir_0",
"Eu substituo."
],
[
"f_substituir_1",
"Tu substituis."
],
[
"f_substituir_2",
"Ele substitui."
],
[
"f_substituir_3",
"Nós substituímos."
],
[
"f_substituir_4",
"Eles substituem."
],
[
"f_sugerir_0",
"Eu sugiro."
],
[
"f_sugerir_1",
"Tu sugeres."
],
[
"f_sugerir_2",
"Ele sugere."
],
[
"f_sugerir_3",
"Nós sugerimos."
],
[
"f_sugerir_4",
"Eles sugerem."
],
[
"f_supor_0",
"Eu suponho."
],
[
"f_supor_1",
"Tu supões."
],
[
"f_supor_2",
"Ele supõe."
],
[
"f_supor_3",
"Nós supomos."
],
[
"f_supor_4",
"Eles supõem."
],
[
"f_ter_0",
"Eu tenho."
],
[
"f_ter_1",
"Tu tens."
],
[
"f_ter_2",
"Ele tem."
],
[
"f_ter_3",
"Nós temos."
],
[
"f_ter_4",
"Eles têm."
],
[
"f_tomar_0",
"Eu tomo."
],
[
"f_tomar_1",
"Tu tomas."
],
[
"f_tomar_2",
"Ele toma."
],
[
"f_tomar_3",
"Nós tomamos."
],
[
"f_tomar_4",
"Eles tomam."
],
[
"f_tossir_0",
"Eu tusso."
],
[
"f_tossir_1",
"Tu tosses."
],
[
"f_tossir_2",
"Ele tosse."
],
[
"f_tossir_3",
"Nós tossimos."
],
[
"f_tossir_4",
"Eles tossem."
],
[
"f_trabalhar_0",
"Eu trabalho."
],
[
"f_trabalhar_1",
"Tu trabalhas."
],
[
"f_trabalhar_2",
"Ele trabalha."
],
[
"f_trabalhar_3",
"Nós trabalhamos."
],
[
"f_trabalhar_4",
"Eles trabalham."
],
[
"f_traduzir_0",
"Eu traduzo."
],
[
"f_traduzir_1",
"Tu traduzes."
],
[
"f_traduzir_2",
"Ele traduz."
],
[
"f_traduzir_3",
"Nós traduzimos."
],
[
"f_traduzir_4",
"Eles traduzem."
],
[
"f_trair_0",
"Eu traio."
],
[
"f_trair_1",
"Tu trais."
],
[
"f_trair_2",
"Ele trai."
],
[
"f_trair_3",
"Nós traímos."
],
[
"f_trair_4",
"Eles traem."
],
[
"f_trazer_0",
"Eu trago."
],
[
"f_trazer_1",
"Tu trazes."
],
[
"f_trazer_2",
"Ele traz."
],
[
"f_trazer_3",
"Nós trazemos."
],
[
"f_trazer_4",
"Eles trazem."
],
[
"f_valer_0",
"Eu valho."
],
[
"f_valer_1",
"Tu vales."
],
[
"f_valer_2",
"Ele vale."
],
[
"f_valer_3",
"Nós valemos."
],
[
"f_valer_4",
"Eles valem."
],
[
"f_varrer_0",
"Eu varro."
],
[
"f_varrer_1",
"Tu varres."
],
[
"f_varrer_2",
"Ele varre."
],
[
"f_varrer_3",
"Nós varremos."
],
[
"f_varrer_4",
"Eles varrem."
],
[
"f_vender_0",
"Eu vendo."
],
[
"f_vender_1",
"Tu vendes."
],
[
"f_vender_2",
"Ele vende."
],
[
"f_vender_3",
"Nós vendemos."
],
[
"f_vender_4",
"Eles vendem."
],
[
"f_ver_0",
"Eu vejo."
],
[
"f_ver_1",
"Tu vês."
],
[
"f_ver_2",
"Ele vê."
],
[
"f_ver_3",
"Nós vemos."
],
[
"f_ver_4",
"Eles veem."
],
[
"f_vestir_0",
"Eu visto."
],
[
"f_vestir_1",
"Tu vestes."
],
[
"f_vestir_2",
"Ele veste."
],
[
"f_vestir_3",
"Nós vestimos."
],
[
"f_vestir_4",
"Eles vestem."
],
[
"f_viajar_0",
"Eu viajo."
],
[
"f_viajar_1",
"Tu viajas."
],
[
"f_viajar_2",
"Ele viaja."
],
[
"f_viajar_3",
"Nós viajamos."
],
[
"f_viajar_4",
"Eles viajam."
],
[
"f_vir_0",
"Eu venho."
],
[
"f_vir_1",
"Tu vens."
],
[
"f_vir_2",
"Ele vem."
],
[
"f_vir_3",
"Nós vimos."
],
[
"f_vir_4",
"Eles vêm."
],
[
"f_visitar_0",
"Eu visito."
],
[
"f_visitar_1",
"Tu visitas."
],
[
"f_visitar_2",
"Ele visita."
],
[
"f_visitar_3",
"Nós visitamos."
],
[
"f_visitar_4",
"Eles visitam."
],
[
"f_viver_0",
"Eu vivo."
],
[
"f_viver_1",
"Tu vives."
],
[
"f_viver_2",
"Ele vive."
],
[
"f_viver_3",
"Nós vivemos."
],
[
"f_viver_4",
"Eles vivem."
],
[
"f_voar_0",
"Eu voo."
],
[
"f_voar_1",
"Tu voas."
],
[
"f_voar_2",
"Ele voa."
],
[
"f_voar_3",
"Nós voamos."
],
[
"f_voar_4",
"Eles voam."
],
[
"f_voltar_0",
"Eu volto."
],
[
"f_voltar_1",
"Tu voltas."
],
[
"f_voltar_2",
"Ele volta."
],
[
"f_voltar_3",
"Nós voltamos."
],
[
"f_voltar_4",
"Eles voltam."
],
[
"h_001",
"A avó Rosa acorda sempre às sete."
],
[
"h_002",
"Avó, tu acordas muito cedo!"
],
[
"h_003",
"Eu durmo pouco, querida. Na minha idade é assim."
],
[
"h_004",
"A Carmen dorme até às oito e meia."
],
[
"h_005",
"A Carmen odeia acordar cedo."
],
[
"h_006",
"Eu prefiro café com leite. E tu, avó?"
],
[
"h_007",
"Eu bebo chá. O café não me faz bem."
],
[
"h_008",
"A Carmen veste o casaco amarelo."
],
[
"h_009",
"Eu saio às nove e volto às seis."
],
[
"h_010",
"Da janela, a avó vê os telhados e o elétrico."
],
[
"h_011",
"Hoje eu vou de elétrico para o estágio."
],
[
"h_012",
"O estágio da Carmen começa às nove e meia."
],
[
"h_013",
"Eu perco sempre o elétrico das nove!"
],
[
"h_014",
"A Carmen almoça com os colegas do estágio."
],
[
"h_015",
"Os colegas da Carmen trabalham muito."
],
[
"h_016",
"Avó, eu conheço uma rapariga de Coimbra no estágio!"
],
[
"h_017",
"A avó mora na Rua da Alegria, em Lisboa."
],
[
"h_018",
"A avó põe os óculos para ler o jornal."
],
[
"h_019",
"Depois, lê o jornal na poltrona da sala."
],
[
"h_020",
"A avó perde sempre os óculos!"
],
[
"h_021",
"À tarde, a avó ouve rádio."
],
[
"h_022",
"Às vezes, a vizinha vem tomar chá com ela."
],
[
"h_023",
"As duas riem muito com as histórias do bairro."
],
[
"h_024",
"A avó conhece todos os vizinhos da rua."
],
[
"h_025",
"No inverno, a avó protege as plantas do frio."
],
[
"h_026",
"A avó cobre a poltrona com uma manta."
],
[
"h_027",
"As plantas da avó crescem muito na janela."
],
[
"h_028",
"O gato da vizinha foge sempre para o telhado."
],
[
"h_029",
"A Carmen volta a casa às seis."
],
[
"h_030",
"Avó, eu trago o pão!"
],
[
"h_031",
"Eu tenho oitenta anos, mas ainda subo as escadas sozinha!"
],
[
"h_032",
"A avó sobe as escadas devagar."
],
[
"h_033",
"Tu tens muitos retratos na sala, avó!"
],
[
"h_034",
"A avó mostra os retratos da família à Carmen."
],
[
"h_035",
"A avó conta histórias da família."
],
[
"h_036",
"Na sala há retratos de toda a família."
],
[
"h_037",
"Na sala já não cabe mais retratos!"
],
[
"h_038",
"Eu sinto saudades de Sevilha, mas gosto muito de Lisboa."
],
[
"h_039",
"Tu falas português muito bem!"
],
[
"h_040",
"Obrigada, avó, mas eu esqueço sempre os acentos!"
],
[
"h_041",
"A avó corrige o português da Carmen com paciência."
],
[
"h_042",
"A Carmen aprende palavras novas com a avó."
],
[
"h_043",
"A Carmen repete as palavras novas em voz alta."
],
[
"h_044",
"Hoje eu faço o jantar, avó. Tu descansas!"
],
[
"h_045",
"Eu também ponho a mesa."
],
[
"h_046",
"Obrigada, querida. Tu és um amor."
],
[
"h_047",
"A avó serve a sopa em pratos antigos."
],
[
"h_048",
"As duas comem a sopa na sala."
],
[
"h_049",
"Em Lisboa, nós jantamos às oito."
],
[
"h_050",
"Em Sevilha, nós jantamos mais tarde."
],
[
"h_051",
"Avó, eu penso que tu cozinhas muito bem!"
],
[
"h_052",
"Eu quero aprender a fazer esta sopa."
],
[
"h_053",
"A avó diz que não come doces, mas mente!"
],
[
"h_054",
"Eu posso lavar a loiça?"
],
[
"h_055",
"Avó, eu não ouço bem: a rua tem muito barulho."
],
[
"h_056",
"Avó, tu entendes as minhas mensagens com emojis?"
],
[
"h_057",
"Não entendo nada, mas acho graça!"
],
[
"h_058",
"Antes de dormir, a avó fecha as janelas."
],
[
"h_059",
"Boa noite, avó. Eu estou muito cansada."
],
[
"h_060",
"Ao sábado, nós passeamos pelo bairro."
],
[
"h_061",
"Ao domingo, as duas passeiam junto ao rio."
],
[
"h_062",
"Eu durmo muito bem nesta casa, avó."
],
[
"h_063",
"Avó, tu queres ir ao cinema?"
],
[
"h_064",
"Eu posso ir, mas só à tarde."
],
[
"h_065",
"E tu preferes um filme português ou espanhol?"
],
[
"h_066",
"Ao sábado, as duas compram fruta no mercado."
],
[
"h_067",
"As duas descem a rua devagar."
],
[
"h_068",
"Ao domingo à tarde, as duas jogam às cartas."
],
[
"h_069",
"Tu jogas muito bem, avó!"
],
[
"h_070",
"Tu sentes frio, avó?"
],
[
"h_071",
"A Carmen penteia a avó antes de sair."
],
[
"h_072",
"A avó sorri quando vê os retratos."
],
[
"h_073",
"A Carmen propõe um passeio de elétrico."
],
[
"h_074",
"Avó, os meus colegas querem conhecer-te!"
],
[
"h_075",
"Eles vêm jantar no sábado."
],
[
"h_076",
"Avó, eu peço desculpa pelo barulho no sábado."
],
[
"h_077",
"A Carmen traduz as palavras difíceis para os colegas."
],
[
"h_078",
"Eu traduzo as tuas mensagens para a minha irmã."
],
[
"h_079",
"A Carmen oferece flores à avó."
],
[
"h_080",
"A avó agradece as flores com um beijinho."
],
[
"h_081",
"Para a avó, uma visita da neta vale mais do que tudo!"
],
[
"h_082",
"Avó, tu contas histórias muito divertidas!"
],
[
"h_083",
"Não encontro a chave de casa!"
],
[
"h_084",
"Amanhã eu começo às nove e meia."
],
[
"h_085",
"Ao domingo, a Carmen escreve uma mensagem à mãe."
],
[
"h_086",
"A Carmen não conduz em Lisboa: anda de elétrico."
],
[
"h_087",
"Em Lisboa, a Carmen descobre coisas novas todos os dias."
],
[
"h_088",
"Com o casaco amarelo, a Carmen parece uma lisboeta!"
]
],
"br": [
[
"f_abrir_0",
"Eu abro."
],
[
"f_abrir_2",
"Você abre."
],
[
"f_abrir_3",
"Nós abrimos."
],
[
"f_abrir_4",
"Vocês abrem."
],
[
"f_acabar_0",
"Eu acabo."
],
[
"f_acabar_2",
"Você acaba."
],
[
"f_acabar_3",
"Nós acabamos."
],
[
"f_acabar_4",
"Vocês acabam."
],
[
"f_acender_0",
"Eu acendo."
],
[
"f_acender_2",
"Você acende."
],
[
"f_acender_3",
"Nós acendemos."
],
[
"f_acender_4",
"Vocês acendem."
],
[
"f_achar_0",
"Eu acho."
],
[
"f_achar_2",
"Você acha."
],
[
"f_achar_3",
"Nós achamos."
],
[
"f_achar_4",
"Vocês acham."
],
[
"f_acordar_0",
"Eu acordo."
],
[
"f_acordar_2",
"Você acorda."
],
[
"f_acordar_3",
"Nós acordamos."
],
[
"f_acordar_4",
"Vocês acordam."
],
[
"f_acudir_0",
"Eu acudo."
],
[
"f_acudir_2",
"Você acode."
],
[
"f_acudir_3",
"Nós acudimos."
],
[
"f_acudir_4",
"Vocês acodem."
],
[
"f_admitir_0",
"Eu admito."
],
[
"f_admitir_2",
"Você admite."
],
[
"f_admitir_3",
"Nós admitimos."
],
[
"f_admitir_4",
"Vocês admitem."
],
[
"f_agir_0",
"Eu ajo."
],
[
"f_agir_2",
"Você age."
],
[
"f_agir_3",
"Nós agimos."
],
[
"f_agir_4",
"Vocês agem."
],
[
"f_agradecer_0",
"Eu agradeço."
],
[
"f_agradecer_2",
"Você agradece."
],
[
"f_agradecer_3",
"Nós agradecemos."
],
[
"f_agradecer_4",
"Vocês agradecem."
],
[
"f_ajudar_0",
"Eu ajudo."
],
[
"f_ajudar_2",
"Você ajuda."
],
[
"f_ajudar_3",
"Nós ajudamos."
],
[
"f_ajudar_4",
"Vocês ajudam."
],
[
"f_almocar_0",
"Eu almoço."
],
[
"f_almocar_2",
"Você almoça."
],
[
"f_almocar_3",
"Nós almoçamos."
],
[
"f_almocar_4",
"Vocês almoçam."
],
[
"f_alugar_0",
"Eu alugo."
],
[
"f_alugar_2",
"Você aluga."
],
[
"f_alugar_3",
"Nós alugamos."
],
[
"f_alugar_4",
"Vocês alugam."
],
[
"f_andar_0",
"Eu ando."
],
[
"f_andar_2",
"Você anda."
],
[
"f_andar_3",
"Nós andamos."
],
[
"f_andar_4",
"Vocês andam."
],
[
"f_ansiar_0",
"Eu anseio."
],
[
"f_ansiar_2",
"Você anseia."
],
[
"f_ansiar_3",
"Nós ansiamos."
],
[
"f_ansiar_4",
"Vocês anseiam."
],
[
"f_aparecer_0",
"Eu apareço."
],
[
"f_aparecer_2",
"Você aparece."
],
[
"f_aparecer_3",
"Nós aparecemos."
],
[
"f_aparecer_4",
"Vocês aparecem."
],
[
"f_aprender_0",
"Eu aprendo."
],
[
"f_aprender_2",
"Você aprende."
],
[
"f_aprender_3",
"Nós aprendemos."
],
[
"f_aprender_4",
"Vocês aprendem."
],
[
"f_arrumar_0",
"Eu arrumo."
],
[
"f_arrumar_2",
"Você arruma."
],
[
"f_arrumar_3",
"Nós arrumamos."
],
[
"f_arrumar_4",
"Vocês arrumam."
],
[
"f_assistir_0",
"Eu assisto."
],
[
"f_assistir_2",
"Você assiste."
],
[
"f_assistir_3",
"Nós assistimos."
],
[
"f_assistir_4",
"Vocês assistem."
],
[
"f_atrair_0",
"Eu atraio."
],
[
"f_atrair_2",
"Você atrai."
],
[
"f_atrair_3",
"Nós atraímos."
],
[
"f_atrair_4",
"Vocês atraem."
],
[
"f_atravessar_0",
"Eu atravesso."
],
[
"f_atravessar_2",
"Você atravessa."
],
[
"f_atravessar_3",
"Nós atravessamos."
],
[
"f_atravessar_4",
"Vocês atravessam."
],
[
"f_atribuir_0",
"Eu atribuo."
],
[
"f_atribuir_2",
"Você atribui."
],
[
"f_atribuir_3",
"Nós atribuímos."
],
[
"f_atribuir_4",
"Vocês atribuem."
],
[
"f_barbear_0",
"Eu barbeio."
],
[
"f_barbear_2",
"Você barbeia."
],
[
"f_barbear_3",
"Nós barbeamos."
],
[
"f_barbear_4",
"Vocês barbeiam."
],
[
"f_bater_0",
"Eu bato."
],
[
"f_bater_2",
"Você bate."
],
[
"f_bater_3",
"Nós batemos."
],
[
"f_bater_4",
"Vocês batem."
],
[
"f_beber_0",
"Eu bebo."
],
[
"f_beber_2",
"Você bebe."
],
[
"f_beber_3",
"Nós bebemos."
],
[
"f_beber_4",
"Vocês bebem."
],
[
"f_caber_0",
"Eu caibo."
],
[
"f_caber_2",
"Você cabe."
],
[
"f_caber_3",
"Nós cabemos."
],
[
"f_caber_4",
"Vocês cabem."
],
[
"f_cair_0",
"Eu caio."
],
[
"f_cair_2",
"Você cai."
],
[
"f_cair_3",
"Nós caímos."
],
[
"f_cair_4",
"Vocês caem."
],
[
"f_cantar_0",
"Eu canto."
],
[
"f_cantar_2",
"Você canta."
],
[
"f_cantar_3",
"Nós cantamos."
],
[
"f_cantar_4",
"Vocês cantam."
],
[
"f_chatear_0",
"Eu chateio."
],
[
"f_chatear_2",
"Você chateia."
],
[
"f_chatear_3",
"Nós chateamos."
],
[
"f_chatear_4",
"Vocês chateiam."
],
[
"f_chegar_0",
"Eu chego."
],
[
"f_chegar_2",
"Você chega."
],
[
"f_chegar_3",
"Nós chegamos."
],
[
"f_chegar_4",
"Vocês chegam."
],
[
"f_cobrir_0",
"Eu cubro."
],
[
"f_cobrir_2",
"Você cobre."
],
[
"f_cobrir_3",
"Nós cobrimos."
],
[
"f_cobrir_4",
"Vocês cobrem."
],
[
"f_comecar_0",
"Eu começo."
],
[
"f_comecar_2",
"Você começa."
],
[
"f_comecar_3",
"Nós começamos."
],
[
"f_comecar_4",
"Vocês começam."
],
[
"f_comer_0",
"Eu como."
],
[
"f_comer_2",
"Você come."
],
[
"f_comer_3",
"Nós comemos."
],
[
"f_comer_4",
"Vocês comem."
],
[
"f_compor_0",
"Eu componho."
],
[
"f_compor_2",
"Você compõe."
],
[
"f_compor_3",
"Nós compomos."
],
[
"f_compor_4",
"Vocês compõem."
],
[
"f_comprar_0",
"Eu compro."
],
[
"f_comprar_2",
"Você compra."
],
[
"f_comprar_3",
"Nós compramos."
],
[
"f_comprar_4",
"Vocês compram."
],
[
"f_compreender_0",
"Eu compreendo."
],
[
"f_compreender_2",
"Você compreende."
],
[
"f_compreender_3",
"Nós compreendemos."
],
[
"f_compreender_4",
"Vocês compreendem."
],
[
"f_concluir_0",
"Eu concluo."
],
[
"f_concluir_2",
"Você conclui."
],
[
"f_concluir_3",
"Nós concluímos."
],
[
"f_concluir_4",
"Vocês concluem."
],
[
"f_conduzir_0",
"Eu conduzo."
],
[
"f_conduzir_2",
"Você conduz."
],
[
"f_conduzir_3",
"Nós conduzimos."
],
[
"f_conduzir_4",
"Vocês conduzem."
],
[
"f_confessar_0",
"Eu confesso."
],
[
"f_confessar_2",
"Você confessa."
],
[
"f_confessar_3",
"Nós confessamos."
],
[
"f_confessar_4",
"Vocês confessam."
],
[
"f_conhecer_0",
"Eu conheço."
],
[
"f_conhecer_2",
"Você conhece."
],
[
"f_conhecer_3",
"Nós conhecemos."
],
[
"f_conhecer_4",
"Vocês conhecem."
],
[
"f_conseguir_0",
"Eu consigo."
],
[
"f_conseguir_2",
"Você consegue."
],
[
"f_conseguir_3",
"Nós conseguimos."
],
[
"f_conseguir_4",
"Vocês conseguem."
],
[
"f_construir_0",
"Eu construo."
],
[
"f_construir_2",
"Você constrói."
],
[
"f_construir_3",
"Nós construímos."
],
[
"f_construir_4",
"Vocês constroem."
],
[
"f_consumir_0",
"Eu consumo."
],
[
"f_consumir_2",
"Você consome."
],
[
"f_consumir_3",
"Nós consumimos."
],
[
"f_consumir_4",
"Vocês consomem."
],
[
"f_contar_0",
"Eu conto."
],
[
"f_contar_2",
"Você conta."
],
[
"f_contar_3",
"Nós contamos."
],
[
"f_contar_4",
"Vocês contam."
],
[
"f_conter_0",
"Eu contenho."
],
[
"f_conter_2",
"Você contém."
],
[
"f_conter_3",
"Nós contemos."
],
[
"f_conter_4",
"Vocês contêm."
],
[
"f_contradizer_0",
"Eu contradigo."
],
[
"f_contradizer_2",
"Você contradiz."
],
[
"f_contradizer_3",
"Nós contradizemos."
],
[
"f_contradizer_4",
"Vocês contradizem."
],
[
"f_contribuir_0",
"Eu contribuo."
],
[
"f_contribuir_2",
"Você contribui."
],
[
"f_contribuir_3",
"Nós contribuímos."
],
[
"f_contribuir_4",
"Vocês contribuem."
],
[
"f_convir_0",
"Eu convenho."
],
[
"f_convir_2",
"Você convém."
],
[
"f_convir_3",
"Nós convimos."
],
[
"f_convir_4",
"Vocês convêm."
],
[
"f_correr_0",
"Eu corro."
],
[
"f_correr_2",
"Você corre."
],
[
"f_correr_3",
"Nós corremos."
],
[
"f_correr_4",
"Vocês correm."
],
[
"f_corrigir_0",
"Eu corrijo."
],
[
"f_corrigir_2",
"Você corrige."
],
[
"f_corrigir_3",
"Nós corrigimos."
],
[
"f_corrigir_4",
"Vocês corrigem."
],
[
"f_corroer_0",
"Eu corroo."
],
[
"f_corroer_2",
"Você corrói."
],
[
"f_corroer_3",
"Nós corroemos."
],
[
"f_corroer_4",
"Vocês corroem."
],
[
"f_cozinhar_0",
"Eu cozinho."
],
[
"f_cozinhar_2",
"Você cozinha."
],
[
"f_cozinhar_3",
"Nós cozinhamos."
],
[
"f_cozinhar_4",
"Vocês cozinham."
],
[
"f_crer_0",
"Eu creio."
],
[
"f_crer_2",
"Você crê."
],
[
"f_crer_3",
"Nós cremos."
],
[
"f_crer_4",
"Vocês creem."
],
[
"f_crescer_0",
"Eu cresço."
],
[
"f_crescer_2",
"Você cresce."
],
[
"f_crescer_3",
"Nós crescemos."
],
[
"f_crescer_4",
"Vocês crescem."
],
[
"f_cuspir_0",
"Eu cuspo."
],
[
"f_cuspir_2",
"Você cospe."
],
[
"f_cuspir_3",
"Nós cuspimos."
],
[
"f_cuspir_4",
"Vocês cospem."
],
[
"f_custar_0",
"Eu custo."
],
[
"f_custar_2",
"Você custa."
],
[
"f_custar_3",
"Nós custamos."
],
[
"f_custar_4",
"Vocês custam."
],
[
"f_dancar_0",
"Eu danço."
],
[
"f_dancar_2",
"Você dança."
],
[
"f_dancar_3",
"Nós dançamos."
],
[
"f_dancar_4",
"Vocês dançam."
],
[
"f_dar_0",
"Eu dou."
],
[
"f_dar_2",
"Você dá."
],
[
"f_dar_3",
"Nós damos."
],
[
"f_dar_4",
"Vocês dão."
],
[
"f_decidir_0",
"Eu decido."
],
[
"f_decidir_2",
"Você decide."
],
[
"f_decidir_3",
"Nós decidimos."
],
[
"f_decidir_4",
"Vocês decidem."
],
[
"f_deduzir_0",
"Eu deduzo."
],
[
"f_deduzir_2",
"Você deduz."
],
[
"f_deduzir_3",
"Nós deduzimos."
],
[
"f_deduzir_4",
"Vocês deduzem."
],
[
"f_defender_0",
"Eu defendo."
],
[
"f_defender_2",
"Você defende."
],
[
"f_defender_3",
"Nós defendemos."
],
[
"f_defender_4",
"Vocês defendem."
],
[
"f_deixar_0",
"Eu deixo."
],
[
"f_deixar_2",
"Você deixa."
],
[
"f_deixar_3",
"Nós deixamos."
],
[
"f_deixar_4",
"Vocês deixam."
],
[
"f_depender_0",
"Eu dependo."
],
[
"f_depender_2",
"Você depende."
],
[
"f_depender_3",
"Nós dependemos."
],
[
"f_depender_4",
"Vocês dependem."
],
[
"f_descer_0",
"Eu desço."
],
[
"f_descer_2",
"Você desce."
],
[
"f_descer_3",
"Nós descemos."
],
[
"f_descer_4",
"Vocês descem."
],
[
"f_descobrir_0",
"Eu descubro."
],
[
"f_descobrir_2",
"Você descobre."
],
[
"f_descobrir_3",
"Nós descobrimos."
],
[
"f_descobrir_4",
"Vocês descobrem."
],
[
"f_desfazer_0",
"Eu desfaço."
],
[
"f_desfazer_2",
"Você desfaz."
],
[
"f_desfazer_3",
"Nós desfazemos."
],
[
"f_desfazer_4",
"Vocês desfazem."
],
[
"f_despedir_0",
"Eu despeço."
],
[
"f_despedir_2",
"Você despede."
],
[
"f_despedir_3",
"Nós despedimos."
],
[
"f_despedir_4",
"Vocês despedem."
],
[
"f_despertar_0",
"Eu desperto."
],
[
"f_despertar_2",
"Você desperta."
],
[
"f_despertar_3",
"Nós despertamos."
],
[
"f_despertar_4",
"Vocês despertam."
],
[
"f_despir_0",
"Eu dispo."
],
[
"f_despir_2",
"Você despe."
],
[
"f_despir_3",
"Nós despimos."
],
[
"f_despir_4",
"Vocês despem."
],
[
"f_destruir_0",
"Eu destruo."
],
[
"f_destruir_2",
"Você destrói."
],
[
"f_destruir_3",
"Nós destruímos."
],
[
"f_destruir_4",
"Vocês destroem."
],
[
"f_deter_0",
"Eu detenho."
],
[
"f_deter_2",
"Você detém."
],
[
"f_deter_3",
"Nós detemos."
],
[
"f_deter_4",
"Vocês detêm."
],
[
"f_devolver_0",
"Eu devolvo."
],
[
"f_devolver_2",
"Você devolve."
],
[
"f_devolver_3",
"Nós devolvemos."
],
[
"f_devolver_4",
"Vocês devolvem."
],
[
"f_diminuir_0",
"Eu diminuo."
],
[
"f_diminuir_2",
"Você diminui."
],
[
"f_diminuir_3",
"Nós diminuímos."
],
[
"f_diminuir_4",
"Vocês diminuem."
],
[
"f_dirigir_0",
"Eu dirijo."
],
[
"f_dirigir_2",
"Você dirige."
],
[
"f_dirigir_3",
"Nós dirigimos."
],
[
"f_dirigir_4",
"Vocês dirigem."
],
[
"f_discutir_0",
"Eu discuto."
],
[
"f_discutir_2",
"Você discute."
],
[
"f_discutir_3",
"Nós discutimos."
],
[
"f_discutir_4",
"Vocês discutem."
],
[
"f_dispor_0",
"Eu disponho."
],
[
"f_dispor_2",
"Você dispõe."
],
[
"f_dispor_3",
"Nós dispomos."
],
[
"f_dispor_4",
"Vocês dispõem."
],
[
"f_distrair_0",
"Eu distraio."
],
[
"f_distrair_2",
"Você distrai."
],
[
"f_distrair_3",
"Nós distraímos."
],
[
"f_distrair_4",
"Vocês distraem."
],
[
"f_distribuir_0",
"Eu distribuo."
],
[
"f_distribuir_2",
"Você distribui."
],
[
"f_distribuir_3",
"Nós distribuímos."
],
[
"f_distribuir_4",
"Vocês distribuem."
],
[
"f_divertir_0",
"Eu divirto."
],
[
"f_divertir_2",
"Você diverte."
],
[
"f_divertir_3",
"Nós divertimos."
],
[
"f_divertir_4",
"Vocês divertem."
],
[
"f_dividir_0",
"Eu divido."
],
[
"f_dividir_2",
"Você divide."
],
[
"f_dividir_3",
"Nós dividimos."
],
[
"f_dividir_4",
"Vocês dividem."
],
[
"f_dizer_0",
"Eu digo."
],
[
"f_dizer_2",
"Você diz."
],
[
"f_dizer_3",
"Nós dizemos."
],
[
"f_dizer_4",
"Vocês dizem."
],
[
"f_dormir_0",
"Eu durmo."
],
[
"f_dormir_2",
"Você dorme."
],
[
"f_dormir_3",
"Nós dormimos."
],
[
"f_dormir_4",
"Vocês dormem."
],
[
"f_eleger_0",
"Eu elejo."
],
[
"f_eleger_2",
"Você elege."
],
[
"f_eleger_3",
"Nós elegemos."
],
[
"f_eleger_4",
"Vocês elegem."
],
[
"f_encontrar_0",
"Eu encontro."
],
[
"f_encontrar_2",
"Você encontra."
],
[
"f_encontrar_3",
"Nós encontramos."
],
[
"f_encontrar_4",
"Vocês encontram."
],
[
"f_engolir_0",
"Eu engulo."
],
[
"f_engolir_2",
"Você engole."
],
[
"f_engolir_3",
"Nós engolimos."
],
[
"f_engolir_4",
"Vocês engolem."
],
[
"f_entender_0",
"Eu entendo."
],
[
"f_entender_2",
"Você entende."
],
[
"f_entender_3",
"Nós entendemos."
],
[
"f_entender_4",
"Vocês entendem."
],
[
"f_entrar_0",
"Eu entro."
],
[
"f_entrar_2",
"Você entra."
],
[
"f_entrar_3",
"Nós entramos."
],
[
"f_entrar_4",
"Vocês entram."
],
[
"f_entreter_0",
"Eu entretenho."
],
[
"f_entreter_2",
"Você entretém."
],
[
"f_entreter_3",
"Nós entretemos."
],
[
"f_entreter_4",
"Vocês entretêm."
],
[
"f_entupir_0",
"Eu entupo."
],
[
"f_entupir_2",
"Você entope."
],
[
"f_entupir_3",
"Nós entupimos."
],
[
"f_entupir_4",
"Vocês entopem."
],
[
"f_escolher_0",
"Eu escolho."
],
[
"f_escolher_2",
"Você escolhe."
],
[
"f_escolher_3",
"Nós escolhemos."
],
[
"f_escolher_4",
"Vocês escolhem."
],
[
"f_escrever_0",
"Eu escrevo."
],
[
"f_escrever_2",
"Você escreve."
],
[
"f_escrever_3",
"Nós escrevemos."
],
[
"f_escrever_4",
"Vocês escrevem."
],
[
"f_esperar_0",
"Eu espero."
],
[
"f_esperar_2",
"Você espera."
],
[
"f_esperar_3",
"Nós esperamos."
],
[
"f_esperar_4",
"Vocês esperam."
],
[
"f_esquecer_0",
"Eu esqueço."
],
[
"f_esquecer_2",
"Você esquece."
],
[
"f_esquecer_3",
"Nós esquecemos."
],
[
"f_esquecer_4",
"Vocês esquecem."
],
[
"f_estabelecer_0",
"Eu estabeleço."
],
[
"f_estabelecer_2",
"Você estabelece."
],
[
"f_estabelecer_3",
"Nós estabelecemos."
],
[
"f_estabelecer_4",
"Vocês estabelecem."
],
[
"f_estar_0",
"Eu estou."
],
[
"f_estar_2",
"Você está."
],
[
"f_estar_3",
"Nós estamos."
],
[
"f_estar_4",
"Vocês estão."
],
[
"f_estrear_0",
"Eu estreio."
],
[
"f_estrear_2",
"Você estreia."
],
[
"f_estrear_3",
"Nós estreamos."
],
[
"f_estrear_4",
"Vocês estreiam."
],
[
"f_estudar_0",
"Eu estudo."
],
[
"f_estudar_2",
"Você estuda."
],
[
"f_estudar_3",
"Nós estudamos."
],
[
"f_estudar_4",
"Vocês estudam."
],
[
"f_exigir_0",
"Eu exijo."
],
[
"f_exigir_2",
"Você exige."
],
[
"f_exigir_3",
"Nós exigimos."
],
[
"f_exigir_4",
"Vocês exigem."
],
[
"f_existir_0",
"Eu existo."
],
[
"f_existir_2",
"Você existe."
],
[
"f_existir_3",
"Nós existimos."
],
[
"f_existir_4",
"Vocês existem."
],
[
"f_expor_0",
"Eu exponho."
],
[
"f_expor_2",
"Você expõe."
],
[
"f_expor_3",
"Nós expomos."
],
[
"f_expor_4",
"Vocês expõem."
],
[
"f_falar_0",
"Eu falo."
],
[
"f_falar_2",
"Você fala."
],
[
"f_falar_3",
"Nós falamos."
],
[
"f_falar_4",
"Vocês falam."
],
[
"f_fazer_0",
"Eu faço."
],
[
"f_fazer_2",
"Você faz."
],
[
"f_fazer_3",
"Nós fazemos."
],
[
"f_fazer_4",
"Vocês fazem."
],
[
"f_fechar_0",
"Eu fecho."
],
[
"f_fechar_2",
"Você fecha."
],
[
"f_fechar_3",
"Nós fechamos."
],
[
"f_fechar_4",
"Vocês fecham."
],
[
"f_ferir_0",
"Eu firo."
],
[
"f_ferir_2",
"Você fere."
],
[
"f_ferir_3",
"Nós ferimos."
],
[
"f_ferir_4",
"Vocês ferem."
],
[
"f_ficar_0",
"Eu fico."
],
[
"f_ficar_2",
"Você fica."
],
[
"f_ficar_3",
"Nós ficamos."
],
[
"f_ficar_4",
"Vocês ficam."
],
[
"f_fingir_0",
"Eu finjo."
],
[
"f_fingir_2",
"Você finge."
],
[
"f_fingir_3",
"Nós fingimos."
],
[
"f_fingir_4",
"Vocês fingem."
],
[
"f_fugir_0",
"Eu fujo."
],
[
"f_fugir_2",
"Você foge."
],
[
"f_fugir_3",
"Nós fugimos."
],
[
"f_fugir_4",
"Vocês fogem."
],
[
"f_garantir_0",
"Eu garanto."
],
[
"f_garantir_2",
"Você garante."
],
[
"f_garantir_3",
"Nós garantimos."
],
[
"f_garantir_4",
"Vocês garantem."
],
[
"f_gostar_0",
"Eu gosto."
],
[
"f_gostar_2",
"Você gosta."
],
[
"f_gostar_3",
"Nós gostamos."
],
[
"f_gostar_4",
"Vocês gostam."
],
[
"f_haver_0",
"Eu hei."
],
[
"f_haver_2",
"Você há."
],
[
"f_haver_3",
"Nós havemos."
],
[
"f_haver_4",
"Vocês hão."
],
[
"f_impedir_0",
"Eu impeço."
],
[
"f_impedir_2",
"Você impede."
],
[
"f_impedir_3",
"Nós impedimos."
],
[
"f_impedir_4",
"Vocês impedem."
],
[
"f_impor_0",
"Eu imponho."
],
[
"f_impor_2",
"Você impõe."
],
[
"f_impor_3",
"Nós impomos."
],
[
"f_impor_4",
"Vocês impõem."
],
[
"f_imprimir_0",
"Eu imprimo."
],
[
"f_imprimir_2",
"Você imprime."
],
[
"f_imprimir_3",
"Nós imprimimos."
],
[
"f_imprimir_4",
"Vocês imprimem."
],
[
"f_incendiar_0",
"Eu incendeio."
],
[
"f_incendiar_2",
"Você incendeia."
],
[
"f_incendiar_3",
"Nós incendiamos."
],
[
"f_incendiar_4",
"Vocês incendeiam."
],
[
"f_incluir_0",
"Eu incluo."
],
[
"f_incluir_2",
"Você inclui."
],
[
"f_incluir_3",
"Nós incluímos."
],
[
"f_incluir_4",
"Vocês incluem."
],
[
"f_insistir_0",
"Eu insisto."
],
[
"f_insistir_2",
"Você insiste."
],
[
"f_insistir_3",
"Nós insistimos."
],
[
"f_insistir_4",
"Vocês insistem."
],
[
"f_intervir_0",
"Eu intervenho."
],
[
"f_intervir_2",
"Você intervém."
],
[
"f_intervir_3",
"Nós intervimos."
],
[
"f_intervir_4",
"Vocês intervêm."
],
[
"f_introduzir_0",
"Eu introduzo."
],
[
"f_introduzir_2",
"Você introduz."
],
[
"f_introduzir_3",
"Nós introduzimos."
],
[
"f_introduzir_4",
"Vocês introduzem."
],
[
"f_investir_0",
"Eu invisto."
],
[
"f_investir_2",
"Você investe."
],
[
"f_investir_3",
"Nós investimos."
],
[
"f_investir_4",
"Vocês investem."
],
[
"f_ir_0",
"Eu vou."
],
[
"f_ir_2",
"Você vai."
],
[
"f_ir_3",
"Nós vamos."
],
[
"f_ir_4",
"Vocês vão."
],
[
"f_jantar_0",
"Eu janto."
],
[
"f_jantar_2",
"Você janta."
],
[
"f_jantar_3",
"Nós jantamos."
],
[
"f_jantar_4",
"Vocês jantam."
],
[
"f_jogar_0",
"Eu jogo."
],
[
"f_jogar_2",
"Você joga."
],
[
"f_jogar_3",
"Nós jogamos."
],
[
"f_jogar_4",
"Vocês jogam."
],
[
"f_lavar_0",
"Eu lavo."
],
[
"f_lavar_2",
"Você lava."
],
[
"f_lavar_3",
"Nós lavamos."
],
[
"f_lavar_4",
"Vocês lavam."
],
[
"f_ler_0",
"Eu leio."
],
[
"f_ler_2",
"Você lê."
],
[
"f_ler_3",
"Nós lemos."
],
[
"f_ler_4",
"Vocês leem."
],
[
"f_levar_0",
"Eu levo."
],
[
"f_levar_2",
"Você leva."
],
[
"f_levar_3",
"Nós levamos."
],
[
"f_levar_4",
"Vocês levam."
],
[
"f_ligar_0",
"Eu ligo."
],
[
"f_ligar_2",
"Você liga."
],
[
"f_ligar_3",
"Nós ligamos."
],
[
"f_ligar_4",
"Vocês ligam."
],
[
"f_limpar_0",
"Eu limpo."
],
[
"f_limpar_2",
"Você limpa."
],
[
"f_limpar_3",
"Nós limpamos."
],
[
"f_limpar_4",
"Vocês limpam."
],
[
"f_manter_0",
"Eu mantenho."
],
[
"f_manter_2",
"Você mantém."
],
[
"f_manter_3",
"Nós mantemos."
],
[
"f_manter_4",
"Vocês mantêm."
],
[
"f_mediar_0",
"Eu medeio."
],
[
"f_mediar_2",
"Você medeia."
],
[
"f_mediar_3",
"Nós mediamos."
],
[
"f_mediar_4",
"Vocês medeiam."
],
[
"f_medir_0",
"Eu meço."
],
[
"f_medir_2",
"Você mede."
],
[
"f_medir_3",
"Nós medimos."
],
[
"f_medir_4",
"Vocês medem."
],
[
"f_mentir_0",
"Eu minto."
],
[
"f_mentir_2",
"Você mente."
],
[
"f_mentir_3",
"Nós mentimos."
],
[
"f_mentir_4",
"Vocês mentem."
],
[
"f_merecer_0",
"Eu mereço."
],
[
"f_merecer_2",
"Você merece."
],
[
"f_merecer_3",
"Nós merecemos."
],
[
"f_merecer_4",
"Vocês merecem."
],
[
"f_meter_0",
"Eu meto."
],
[
"f_meter_2",
"Você mete."
],
[
"f_meter_3",
"Nós metemos."
],
[
"f_meter_4",
"Vocês metem."
],
[
"f_moer_0",
"Eu moo."
],
[
"f_moer_2",
"Você mói."
],
[
"f_moer_3",
"Nós moemos."
],
[
"f_moer_4",
"Vocês moem."
],
[
"f_morar_0",
"Eu moro."
],
[
"f_morar_2",
"Você mora."
],
[
"f_morar_3",
"Nós moramos."
],
[
"f_morar_4",
"Vocês moram."
],
[
"f_mostrar_0",
"Eu mostro."
],
[
"f_mostrar_2",
"Você mostra."
],
[
"f_mostrar_3",
"Nós mostramos."
],
[
"f_mostrar_4",
"Vocês mostram."
],
[
"f_mover_0",
"Eu movo."
],
[
"f_mover_2",
"Você move."
],
[
"f_mover_3",
"Nós movemos."
],
[
"f_mover_4",
"Vocês movem."
],
[
"f_mudar_0",
"Eu mudo."
],
[
"f_mudar_2",
"Você muda."
],
[
"f_mudar_3",
"Nós mudamos."
],
[
"f_mudar_4",
"Vocês mudam."
],
[
"f_nadar_0",
"Eu nado."
],
[
"f_nadar_2",
"Você nada."
],
[
"f_nadar_3",
"Nós nadamos."
],
[
"f_nadar_4",
"Vocês nadam."
],
[
"f_nascer_0",
"Eu nasço."
],
[
"f_nascer_2",
"Você nasce."
],
[
"f_nascer_3",
"Nós nascemos."
],
[
"f_nascer_4",
"Vocês nascem."
],
[
"f_negar_0",
"Eu nego."
],
[
"f_negar_2",
"Você nega."
],
[
"f_negar_3",
"Nós negamos."
],
[
"f_negar_4",
"Vocês negam."
],
[
"f_nomear_0",
"Eu nomeio."
],
[
"f_nomear_2",
"Você nomeia."
],
[
"f_nomear_3",
"Nós nomeamos."
],
[
"f_nomear_4",
"Vocês nomeiam."
],
[
"f_obedecer_0",
"Eu obedeço."
],
[
"f_obedecer_2",
"Você obedece."
],
[
"f_obedecer_3",
"Nós obedecemos."
],
[
"f_obedecer_4",
"Vocês obedecem."
],
[
"f_obter_0",
"Eu obtenho."
],
[
"f_obter_2",
"Você obtém."
],
[
"f_obter_3",
"Nós obtemos."
],
[
"f_obter_4",
"Vocês obtêm."
],
[
"f_odiar_0",
"Eu odeio."
],
[
"f_odiar_2",
"Você odeia."
],
[
"f_odiar_3",
"Nós odiamos."
],
[
"f_odiar_4",
"Vocês odeiam."
],
[
"f_oferecer_0",
"Eu ofereço."
],
[
"f_oferecer_2",
"Você oferece."
],
[
"f_oferecer_3",
"Nós oferecemos."
],
[
"f_oferecer_4",
"Vocês oferecem."
],
[
"f_omitir_0",
"Eu omito."
],
[
"f_omitir_2",
"Você omite."
],
[
"f_omitir_3",
"Nós omitimos."
],
[
"f_omitir_4",
"Vocês omitem."
],
[
"f_ouvir_0",
"Eu ouço."
],
[
"f_ouvir_2",
"Você ouve."
],
[
"f_ouvir_3",
"Nós ouvimos."
],
[
"f_ouvir_4",
"Vocês ouvem."
],
[
"f_pagar_0",
"Eu pago."
],
[
"f_pagar_2",
"Você paga."
],
[
"f_pagar_3",
"Nós pagamos."
],
[
"f_pagar_4",
"Vocês pagam."
],
[
"f_parecer_0",
"Eu pareço."
],
[
"f_parecer_2",
"Você parece."
],
[
"f_parecer_3",
"Nós parecemos."
],
[
"f_parecer_4",
"Vocês parecem."
],
[
"f_partir_0",
"Eu parto."
],
[
"f_partir_2",
"Você parte."
],
[
"f_partir_3",
"Nós partimos."
],
[
"f_partir_4",
"Vocês partem."
],
[
"f_passear_0",
"Eu passeio."
],
[
"f_passear_2",
"Você passeia."
],
[
"f_passear_3",
"Nós passeamos."
],
[
"f_passear_4",
"Vocês passeiam."
],
[
"f_pedir_0",
"Eu peço."
],
[
"f_pedir_2",
"Você pede."
],
[
"f_pedir_3",
"Nós pedimos."
],
[
"f_pedir_4",
"Vocês pedem."
],
[
"f_pensar_0",
"Eu penso."
],
[
"f_pensar_2",
"Você pensa."
],
[
"f_pensar_3",
"Nós pensamos."
],
[
"f_pensar_4",
"Vocês pensam."
],
[
"f_pentear_0",
"Eu penteio."
],
[
"f_pentear_2",
"Você penteia."
],
[
"f_pentear_3",
"Nós penteamos."
],
[
"f_pentear_4",
"Vocês penteiam."
],
[
"f_perder_0",
"Eu perco."
],
[
"f_perder_2",
"Você perde."
],
[
"f_perder_3",
"Nós perdemos."
],
[
"f_perder_4",
"Vocês perdem."
],
[
"f_perguntar_0",
"Eu pergunto."
],
[
"f_perguntar_2",
"Você pergunta."
],
[
"f_perguntar_3",
"Nós perguntamos."
],
[
"f_perguntar_4",
"Vocês perguntam."
],
[
"f_permitir_0",
"Eu permito."
],
[
"f_permitir_2",
"Você permite."
],
[
"f_permitir_3",
"Nós permitimos."
],
[
"f_permitir_4",
"Vocês permitem."
],
[
"f_poder_0",
"Eu posso."
],
[
"f_poder_2",
"Você pode."
],
[
"f_poder_3",
"Nós podemos."
],
[
"f_poder_4",
"Vocês podem."
],
[
"f_poluir_0",
"Eu poluo."
],
[
"f_poluir_2",
"Você polui."
],
[
"f_poluir_3",
"Nós poluímos."
],
[
"f_poluir_4",
"Vocês poluem."
],
[
"f_por_0",
"Eu ponho."
],
[
"f_por_2",
"Você põe."
],
[
"f_por_3",
"Nós pomos."
],
[
"f_por_4",
"Vocês põem."
],
[
"f_possuir_0",
"Eu possuo."
],
[
"f_possuir_2",
"Você possui."
],
[
"f_possuir_3",
"Nós possuímos."
],
[
"f_possuir_4",
"Vocês possuem."
],
[
"f_precisar_0",
"Eu preciso."
],
[
"f_precisar_2",
"Você precisa."
],
[
"f_precisar_3",
"Nós precisamos."
],
[
"f_precisar_4",
"Vocês precisam."
],
[
"f_preferir_0",
"Eu prefiro."
],
[
"f_preferir_2",
"Você prefere."
],
[
"f_preferir_3",
"Nós preferimos."
],
[
"f_preferir_4",
"Vocês preferem."
],
[
"f_prever_0",
"Eu prevejo."
],
[
"f_prever_2",
"Você prevê."
],
[
"f_prever_3",
"Nós prevemos."
],
[
"f_prever_4",
"Vocês preveem."
],
[
"f_procurar_0",
"Eu procuro."
],
[
"f_procurar_2",
"Você procura."
],
[
"f_procurar_3",
"Nós procuramos."
],
[
"f_procurar_4",
"Vocês procuram."
],
[
"f_produzir_0",
"Eu produzo."
],
[
"f_produzir_2",
"Você produz."
],
[
"f_produzir_3",
"Nós produzimos."
],
[
"f_produzir_4",
"Vocês produzem."
],
[
"f_propor_0",
"Eu proponho."
],
[
"f_propor_2",
"Você propõe."
],
[
"f_propor_3",
"Nós propomos."
],
[
"f_propor_4",
"Vocês propõem."
],
[
"f_proteger_0",
"Eu protejo."
],
[
"f_proteger_2",
"Você protege."
],
[
"f_proteger_3",
"Nós protegemos."
],
[
"f_proteger_4",
"Vocês protegem."
],
[
"f_provar_0",
"Eu provo."
],
[
"f_provar_2",
"Você prova."
],
[
"f_provar_3",
"Nós provamos."
],
[
"f_provar_4",
"Vocês provam."
],
[
"f_querer_0",
"Eu quero."
],
[
"f_querer_2",
"Você quer."
],
[
"f_querer_3",
"Nós queremos."
],
[
"f_querer_4",
"Vocês querem."
],
[
"f_reagir_0",
"Eu reajo."
],
[
"f_reagir_2",
"Você reage."
],
[
"f_reagir_3",
"Nós reagimos."
],
[
"f_reagir_4",
"Vocês reagem."
],
[
"f_recear_0",
"Eu receio."
],
[
"f_recear_2",
"Você receia."
],
[
"f_recear_3",
"Nós receamos."
],
[
"f_recear_4",
"Vocês receiam."
],
[
"f_receber_0",
"Eu recebo."
],
[
"f_receber_2",
"Você recebe."
],
[
"f_receber_3",
"Nós recebemos."
],
[
"f_receber_4",
"Vocês recebem."
],
[
"f_recomendar_0",
"Eu recomendo."
],
[
"f_recomendar_2",
"Você recomenda."
],
[
"f_recomendar_3",
"Nós recomendamos."
],
[
"f_recomendar_4",
"Vocês recomendam."
],
[
"f_recordar_0",
"Eu recordo."
],
[
"f_recordar_2",
"Você recorda."
],
[
"f_recordar_3",
"Nós recordamos."
],
[
"f_recordar_4",
"Vocês recordam."
],
[
"f_reduzir_0",
"Eu reduzo."
],
[
"f_reduzir_2",
"Você reduz."
],
[
"f_reduzir_3",
"Nós reduzimos."
],
[
"f_reduzir_4",
"Vocês reduzem."
],
[
"f_refazer_0",
"Eu refaço."
],
[
"f_refazer_2",
"Você refaz."
],
[
"f_refazer_3",
"Nós refazemos."
],
[
"f_refazer_4",
"Vocês refazem."
],
[
"f_referir_0",
"Eu refiro."
],
[
"f_referir_2",
"Você refere."
],
[
"f_referir_3",
"Nós referimos."
],
[
"f_referir_4",
"Vocês referem."
],
[
"f_reler_0",
"Eu releio."
],
[
"f_reler_2",
"Você relê."
],
[
"f_reler_3",
"Nós relemos."
],
[
"f_reler_4",
"Vocês releem."
],
[
"f_remediar_0",
"Eu remedeio."
],
[
"f_remediar_2",
"Você remedeia."
],
[
"f_remediar_3",
"Nós remediamos."
],
[
"f_remediar_4",
"Vocês remedeiam."
],
[
"f_repetir_0",
"Eu repito."
],
[
"f_repetir_2",
"Você repete."
],
[
"f_repetir_3",
"Nós repetimos."
],
[
"f_repetir_4",
"Vocês repetem."
],
[
"f_resistir_0",
"Eu resisto."
],
[
"f_resistir_2",
"Você resiste."
],
[
"f_resistir_3",
"Nós resistimos."
],
[
"f_resistir_4",
"Vocês resistem."
],
[
"f_responder_0",
"Eu respondo."
],
[
"f_responder_2",
"Você responde."
],
[
"f_responder_3",
"Nós respondemos."
],
[
"f_responder_4",
"Vocês respondem."
],
[
"f_reter_0",
"Eu retenho."
],
[
"f_reter_2",
"Você retém."
],
[
"f_reter_3",
"Nós retemos."
],
[
"f_reter_4",
"Vocês retêm."
],
[
"f_rever_0",
"Eu revejo."
],
[
"f_rever_2",
"Você revê."
],
[
"f_rever_3",
"Nós revemos."
],
[
"f_rever_4",
"Vocês reveem."
],
[
"f_rir_0",
"Eu rio."
],
[
"f_rir_2",
"Você ri."
],
[
"f_rir_3",
"Nós rimos."
],
[
"f_rir_4",
"Vocês riem."
],
[
"f_roer_0",
"Eu roo."
],
[
"f_roer_2",
"Você rói."
],
[
"f_roer_3",
"Nós roemos."
],
[
"f_roer_4",
"Vocês roem."
],
[
"f_saber_0",
"Eu sei."
],
[
"f_saber_2",
"Você sabe."
],
[
"f_saber_3",
"Nós sabemos."
],
[
"f_saber_4",
"Vocês sabem."
],
[
"f_sacudir_0",
"Eu sacudo."
],
[
"f_sacudir_2",
"Você sacode."
],
[
"f_sacudir_3",
"Nós sacudimos."
],
[
"f_sacudir_4",
"Vocês sacodem."
],
[
"f_sair_0",
"Eu saio."
],
[
"f_sair_2",
"Você sai."
],
[
"f_sair_3",
"Nós saímos."
],
[
"f_sair_4",
"Vocês saem."
],
[
"f_satisfazer_0",
"Eu satisfaço."
],
[
"f_satisfazer_2",
"Você satisfaz."
],
[
"f_satisfazer_3",
"Nós satisfazemos."
],
[
"f_satisfazer_4",
"Vocês satisfazem."
],
[
"f_seguir_0",
"Eu sigo."
],
[
"f_seguir_2",
"Você segue."
],
[
"f_seguir_3",
"Nós seguimos."
],
[
"f_seguir_4",
"Vocês seguem."
],
[
"f_semear_0",
"Eu semeio."
],
[
"f_semear_2",
"Você semeia."
],
[
"f_semear_3",
"Nós semeamos."
],
[
"f_semear_4",
"Vocês semeiam."
],
[
"f_sentar_0",
"Eu sento."
],
[
"f_sentar_2",
"Você senta."
],
[
"f_sentar_3",
"Nós sentamos."
],
[
"f_sentar_4",
"Vocês sentam."
],
[
"f_sentir_0",
"Eu sinto."
],
[
"f_sentir_2",
"Você sente."
],
[
"f_sentir_3",
"Nós sentimos."
],
[
"f_sentir_4",
"Vocês sentem."
],
[
"f_ser_0",
"Eu sou."
],
[
"f_ser_2",
"Você é."
],
[
"f_ser_3",
"Nós somos."
],
[
"f_ser_4",
"Vocês são."
],
[
"f_servir_0",
"Eu sirvo."
],
[
"f_servir_2",
"Você serve."
],
[
"f_servir_3",
"Nós servimos."
],
[
"f_servir_4",
"Vocês servem."
],
[
"f_sonhar_0",
"Eu sonho."
],
[
"f_sonhar_2",
"Você sonha."
],
[
"f_sonhar_3",
"Nós sonhamos."
],
[
"f_sonhar_4",
"Vocês sonham."
],
[
"f_sorrir_0",
"Eu sorrio."
],
[
"f_sorrir_2",
"Você sorri."
],
[
"f_sorrir_3",
"Nós sorrimos."
],
[
"f_sorrir_4",
"Vocês sorriem."
],
[
"f_subir_0",
"Eu subo."
],
[
"f_subir_2",
"Você sobe."
],
[
"f_subir_3",
"Nós subimos."
],
[
"f_subir_4",
"Vocês sobem."
],
[
"f_substituir_0",
"Eu substituo."
],
[
"f_substituir_2",
"Você substitui."
],
[
"f_substituir_3",
"Nós substituímos."
],
[
"f_substituir_4",
"Vocês substituem."
],
[
"f_sugerir_0",
"Eu sugiro."
],
[
"f_sugerir_2",
"Você sugere."
],
[
"f_sugerir_3",
"Nós sugerimos."
],
[
"f_sugerir_4",
"Vocês sugerem."
],
[
"f_supor_0",
"Eu suponho."
],
[
"f_supor_2",
"Você supõe."
],
[
"f_supor_3",
"Nós supomos."
],
[
"f_supor_4",
"Vocês supõem."
],
[
"f_ter_0",
"Eu tenho."
],
[
"f_ter_2",
"Você tem."
],
[
"f_ter_3",
"Nós temos."
],
[
"f_ter_4",
"Vocês têm."
],
[
"f_tomar_0",
"Eu tomo."
],
[
"f_tomar_2",
"Você toma."
],
[
"f_tomar_3",
"Nós tomamos."
],
[
"f_tomar_4",
"Vocês tomam."
],
[
"f_tossir_0",
"Eu tusso."
],
[
"f_tossir_2",
"Você tosse."
],
[
"f_tossir_3",
"Nós tossimos."
],
[
"f_tossir_4",
"Vocês tossem."
],
[
"f_trabalhar_0",
"Eu trabalho."
],
[
"f_trabalhar_2",
"Você trabalha."
],
[
"f_trabalhar_3",
"Nós trabalhamos."
],
[
"f_trabalhar_4",
"Vocês trabalham."
],
[
"f_traduzir_0",
"Eu traduzo."
],
[
"f_traduzir_2",
"Você traduz."
],
[
"f_traduzir_3",
"Nós traduzimos."
],
[
"f_traduzir_4",
"Vocês traduzem."
],
[
"f_trair_0",
"Eu traio."
],
[
"f_trair_2",
"Você trai."
],
[
"f_trair_3",
"Nós traímos."
],
[
"f_trair_4",
"Vocês traem."
],
[
"f_trazer_0",
"Eu trago."
],
[
"f_trazer_2",
"Você traz."
],
[
"f_trazer_3",
"Nós trazemos."
],
[
"f_trazer_4",
"Vocês trazem."
],
[
"f_valer_0",
"Eu valho."
],
[
"f_valer_2",
"Você vale."
],
[
"f_valer_3",
"Nós valemos."
],
[
"f_valer_4",
"Vocês valem."
],
[
"f_varrer_0",
"Eu varro."
],
[
"f_varrer_2",
"Você varre."
],
[
"f_varrer_3",
"Nós varremos."
],
[
"f_varrer_4",
"Vocês varrem."
],
[
"f_vender_0",
"Eu vendo."
],
[
"f_vender_2",
"Você vende."
],
[
"f_vender_3",
"Nós vendemos."
],
[
"f_vender_4",
"Vocês vendem."
],
[
"f_ver_0",
"Eu vejo."
],
[
"f_ver_2",
"Você vê."
],
[
"f_ver_3",
"Nós vemos."
],
[
"f_ver_4",
"Vocês veem."
],
[
"f_vestir_0",
"Eu visto."
],
[
"f_vestir_2",
"Você veste."
],
[
"f_vestir_3",
"Nós vestimos."
],
[
"f_vestir_4",
"Vocês vestem."
],
[
"f_viajar_0",
"Eu viajo."
],
[
"f_viajar_2",
"Você viaja."
],
[
"f_viajar_3",
"Nós viajamos."
],
[
"f_viajar_4",
"Vocês viajam."
],
[
"f_vir_0",
"Eu venho."
],
[
"f_vir_2",
"Você vem."
],
[
"f_vir_3",
"Nós vimos."
],
[
"f_vir_4",
"Vocês vêm."
],
[
"f_visitar_0",
"Eu visito."
],
[
"f_visitar_2",
"Você visita."
],
[
"f_visitar_3",
"Nós visitamos."
],
[
"f_visitar_4",
"Vocês visitam."
],
[
"f_viver_0",
"Eu vivo."
],
[
"f_viver_2",
"Você vive."
],
[
"f_viver_3",
"Nós vivemos."
],
[
"f_viver_4",
"Vocês vivem."
],
[
"f_voar_0",
"Eu voo."
],
[
"f_voar_2",
"Você voa."
],
[
"f_voar_3",
"Nós voamos."
],
[
"f_voar_4",
"Vocês voam."
],
[
"f_voltar_0",
"Eu volto."
],
[
"f_voltar_2",
"Você volta."
],
[
"f_voltar_3",
"Nós voltamos."
],
[
"f_voltar_4",
"Vocês voltam."
],
[
"h_001",
"A Dona Lúcia acorda sempre às seis e meia."
],
[
"h_002",
"A senhora acorda muito cedo, Dona Lúcia!"
],
[
"h_003",
"Eu durmo pouco, querida."
],
[
"h_004",
"A Carmen dorme até as oito."
],
[
"h_005",
"A Carmen odeia acordar cedo."
],
[
"h_006",
"Eu prefiro café com leite no café da manhã."
],
[
"h_007",
"Eu faço um suco de laranja para você."
],
[
"h_008",
"A Carmen veste uma blusa leve: em São Paulo faz calor."
],
[
"h_009",
"Eu saio às oito e meia e volto às seis."
],
[
"h_010",
"Hoje eu vou de metrô para a universidade."
],
[
"h_011",
"A aula da Carmen começa às nove."
],
[
"h_012",
"Eu sempre perco o ônibus das oito!"
],
[
"h_013",
"A Carmen almoça com os colegas no restaurante da universidade."
],
[
"h_014",
"Os filhos da Dona Lúcia trabalham muito."
],
[
"h_015",
"Eu conheço uma menina de Recife na universidade!"
],
[
"h_016",
"A Dona Lúcia mora em São Paulo há trinta anos."
],
[
"h_017",
"A Dona Lúcia lê o jornal na varanda."
],
[
"h_018",
"A Dona Lúcia perde sempre os óculos!"
],
[
"h_019",
"De tarde, a Dona Lúcia ouve samba no rádio."
],
[
"h_020",
"Às vezes, a vizinha vem tomar um cafezinho com ela."
],
[
"h_021",
"As duas riem muito das histórias do bairro."
],
[
"h_022",
"A Dona Lúcia conhece todos os vizinhos da rua."
],
[
"h_023",
"A Dona Lúcia protege as plantas do sol forte."
],
[
"h_024",
"As plantas da varanda crescem muito."
],
[
"h_025",
"O gato da vizinha sempre foge para o telhado."
],
[
"h_026",
"A Carmen volta para casa às seis."
],
[
"h_027",
"Dona Lúcia, eu trago o pão!"
],
[
"h_028",
"Eu tenho três filhos, mas eles moram longe."
],
[
"h_029",
"A Dona Lúcia sobe a escada devagar."
],
[
"h_030",
"A senhora tem muitas fotos na sala!"
],
[
"h_031",
"A Dona Lúcia mostra as fotos da família para a Carmen."
],
[
"h_032",
"A Dona Lúcia conta histórias da família."
],
[
"h_033",
"Eu sinto saudade de Sevilha, mas gosto muito de São Paulo."
],
[
"h_034",
"Você fala português muito bem!"
],
[
"h_035",
"Obrigada, mas eu sempre esqueço os acentos!"
],
[
"h_036",
"A Dona Lúcia corrige o português da Carmen com paciência."
],
[
"h_037",
"A Carmen aprende palavras novas com a Dona Lúcia."
],
[
"h_038",
"A Carmen repete as palavras novas em voz alta."
],
[
"h_039",
"Hoje eu faço o jantar, Dona Lúcia. A senhora descansa!"
],
[
"h_040",
"Eu também ponho a mesa."
],
[
"h_041",
"Obrigada, querida. Você é um amor."
],
[
"h_042",
"A Dona Lúcia serve arroz e feijão."
],
[
"h_043",
"As duas comem na cozinha."
],
[
"h_044",
"Aqui nós jantamos às sete e meia."
],
[
"h_045",
"Em Sevilha, nós jantamos mais tarde."
],
[
"h_046",
"Eu penso que a senhora cozinha muito bem!"
],
[
"h_047",
"Eu quero aprender a fazer este feijão."
],
[
"h_048",
"A Dona Lúcia diz que não come doce, mas mente!"
],
[
"h_049",
"Eu posso lavar a louça?"
],
[
"h_050",
"Eu não ouço bem: a rua tem muito barulho."
],
[
"h_051",
"A senhora entende as minhas mensagens com emojis?"
],
[
"h_052",
"Não entendo nada, mas acho graça!"
],
[
"h_053",
"Antes de dormir, a Dona Lúcia fecha as janelas."
],
[
"h_054",
"Boa noite, Dona Lúcia. Eu estou muito cansada."
],
[
"h_055",
"No sábado, nós passeamos pelo parque."
],
[
"h_056",
"No domingo, as duas passeiam na Avenida Paulista."
],
[
"h_057",
"Eu durmo muito bem nesta casa."
],
[
"h_058",
"A senhora quer ir ao cinema?"
],
[
"h_059",
"Eu posso ir, mas só de tarde."
],
[
"h_060",
"A senhora prefere um filme brasileiro ou espanhol?"
],
[
"h_061",
"No sábado, as duas compram frutas na feira."
],
[
"h_062",
"No domingo de tarde, as duas jogam cartas."
],
[
"h_063",
"A senhora joga muito bem!"
],
[
"h_064",
"A senhora sente calor, Dona Lúcia?"
],
[
"h_065",
"A Dona Lúcia sorri quando vê as fotos dos netos."
],
[
"h_066",
"A Carmen propõe um passeio pelo centro."
],
[
"h_067",
"Dona Lúcia, os meus colegas querem conhecer a senhora!"
],
[
"h_068",
"Eles vêm jantar no sábado."
],
[
"h_069",
"Eu peço desculpa pelo barulho no sábado."
],
[
"h_070",
"A Carmen traduz as palavras difíceis para os colegas."
],
[
"h_071",
"Eu traduzo as mensagens da senhora para a minha irmã."
],
[
"h_072",
"A Carmen oferece flores para a Dona Lúcia."
],
[
"h_073",
"A Dona Lúcia agradece as flores com um abraço."
],
[
"h_074",
"A senhora conta histórias muito divertidas!"
],
[
"h_075",
"Não encontro a chave de casa!"
],
[
"h_076",
"Amanhã eu começo às nove."
],
[
"h_077",
"No domingo, a Carmen escreve uma mensagem para a mãe."
],
[
"h_078",
"A Carmen não conduz em São Paulo: anda de metrô."
],
[
"h_079",
"Em São Paulo, a Carmen descobre coisas novas todo dia."
]
]
}

PASTA = os.path.join(os.path.dirname(os.path.abspath(__file__)), "audios_presente")

async def um(var, nome, texto, sem):
    destino = os.path.join(PASTA, var, nome + ".mp3")
    if os.path.exists(destino) and os.path.getsize(destino) > 1000:
        return True
    async with sem:
        for tentativa in range(4):
            try:
                await edge_tts.Communicate(texto, VOZES[var], rate=VELOCIDADE).save(destino)
                if os.path.getsize(destino) > 1000:
                    return True
            except Exception as e:
                await asyncio.sleep(2 + tentativa * 3)
        print("  Falhou:", var, nome, texto)
        return False

async def main():
    sem = asyncio.Semaphore(4)
    for var in ("pt", "br"):
        os.makedirs(os.path.join(PASTA, var), exist_ok=True)
        lista = ITENS[var]
        print(f"A gerar {len(lista)} audios ({'Portugal' if var=='pt' else 'Brasil'})...")
        feitos = 0
        tarefas = [um(var, n, t, sem) for n, t in lista]
        for t in asyncio.as_completed(tarefas):
            await t
            feitos += 1
            if feitos % 50 == 0 or feitos == len(lista):
                print(f"  {feitos} / {len(lista)}")
    zpath = os.path.join(os.path.dirname(PASTA), "audios_presente.zip")
    with zipfile.ZipFile(zpath, "w", zipfile.ZIP_STORED) as z:
        for raiz, _, fichs in os.walk(PASTA):
            for f in fichs:
                z.write(os.path.join(raiz, f), os.path.relpath(os.path.join(raiz, f), os.path.dirname(PASTA)))
    print("\nPronto! Ficheiro criado:", zpath)
    print("Envie esse ficheiro .zip no chat.")

asyncio.run(main())
